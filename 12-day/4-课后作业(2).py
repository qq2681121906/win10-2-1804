import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
bg = pygame.image.load('./a/1.jpg')
#screen.blit(bg,(0,0))
pygame.display.update()
a = pygame.image.load('./a/2.jpg')
pygame.display.update()
b = pygame.image.load('./a/3.jpg')
pygame.display.update()
c = pygame.image.load('./a/4.jpg')
pygame.display.update()
d = pygame.image.load('./a/5.jpg')
pygame.display.update()
e = pygame.image.load('./a/6.jpg')
pygame.display.update()
f = pygame.image.load('./a/7.jpg')
pygame.display.update()
g = pygame.image.load('./a/8.jpg')
pygame.display.update()

hero = pygame.image.load('./images/hero1.png')
#screen.blit(hero,(350,500))
hero_rect = pygame.Rect(190,500,50,100)
def quit():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("退出游戏...")
			pygame.quit()
			exit()
while True:
	clock.tick(60)
	hero_rect.y-=3
	if hero_rect.y+hero_rect.height<=0:
		hero_rect.y = 600
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)
	pygame.display.update()
	quit()