import pygame, os
from random import randint

class Acid(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
	#path:
		self.path_geral = os.getcwd()
		self.path_image = self.path_geral + "/graphics/objeto/gota.png"
		
	#init:
		self.image = pygame.image.load(self.path_image)
		if randint(0,134)%2==0:
			pass
		else:
			self.image = pygame.transform.flip(self.image, True, False)
		num = randint(7,10)		
		self.image = pygame.transform.scale(self.image, ((int(30*num//10), int(48*num//10))))
		self.rect  = self.image.get_rect(midbottom = pos)
		self.direction = pygame.math.Vector2(0,0)
		self.acid_group  = pygame.sprite.GroupSingle()

	def update(self,x_shift):
		self.rect.x += x_shift
		self.direction.y += 0.3
		self.rect.y += self.direction.y