import pygame
SCREEN_RECT = pygame.Rect(0,0,800,600)
CREATE_ENEMY_EVENT = pygame.USEREVENT
import random
class plansprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		super().__init__()
		#self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed
	def update(self,*args):
		self.rect.y+=self.speed
class Hero(plansprite):
	def __init__(self):
		super().__init__('./images/hero1.png',0)
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 20
		self.bullets = pygame.sprite.Group()
	def update(self):
		self.speed = 10
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_RIGHT]:
			self.rect.x+=self.speed
		if keys_pressed[pygame.K_LEFT]:
			self.rect.x-=self.speed
		if keys_pressed[pygame.K_UP]:
			self.rect.y-=self.speed
		if keys_pressed[pygame.K_DOWN]:
			self.rect.y+=self.speed
		if keys_pressed[pygame.K_x]:
			self.fire()
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		elif self.rect.top < 0:
			self.rect.top = 0
		elif self.rect.bottom > SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom
	def fire(self):
		bullet = Bullet()
		bullet.rect.y = self.rect.y-bullet.rect.height-5
		bullet.rect.centerx = self.rect.centerx
		self.bullets.add(bullet)
class Enemy(plansprite):
	def __init__(self):
		super().__init__('./plan/images/enemy0.png')
		self.speed = random.randint(1,3)
		num = random.randint(0,SCREEN_RECT.width-self.rect.width)
		self.rect.x = num
		self.rect.bottom = 0
	def update(self):
		super().update()
		if self.rect.y>SCREEN_RECT.height:
			self.kill()
class BG(plansprite):
	def __init__(self,flag=False):
		image_name = '.background/images/bg.png'
		#super().__init__(image_name,3)
		if flag:
			self.rect.y = -self.rect.height
	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class Bullet(plansprite):
	def __init__(self):
		super().__init__('./plan/images/bullet-3.gif',-10)
	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()