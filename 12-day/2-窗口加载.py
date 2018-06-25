import pygame
from jingl import *
class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprite()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
    def startgame(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./3306342557.mp3')
        pygame.mixer.music.play()
        while True:
            self.clock.tick(60)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()
    def __create_sprite(self):
        bg = BG()
        bg2 = BG(True)
        self.bg_group = pygame.sprite.Group(bg,bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("退出游戏...")
                pygame.quit()
                exit()
            elif event.type == CREATE_ENEMY_EVENT:
                self.enemy_group.add(Enemy())
                print("敌机出场...")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.hero.fire()
    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            pygame.quit()
            exit()
    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
if __name__ == '__main__':
    plangame = Game()
    plangame.startgame()