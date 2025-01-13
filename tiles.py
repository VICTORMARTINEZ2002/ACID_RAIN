import pygame, os
from configurações import *
from random import randint
from sys import path

#path:C:\Users\VICTOR\Desktop\_UFMA
path_geral    = path[0]
path_rock     = path_geral + "/graphics/terreno/rock.png"
path_barl     = path_geral + "/graphics/objeto/barril.png"
path_post     = path_geral + "/graphics/objeto/poste.png"
path_cabn     = path_geral + "/graphics/objeto/cabana.png"
path_arv1     = path_geral + "/graphics/objeto/arvores/1.png"
path_arv2     = path_geral + "/graphics/objeto/arvores/2.png"
path_arv3     = path_geral + "/graphics/objeto/arvores/3.png"
path_arvf     = path_geral + "/graphics/objeto/arvores/f.png"
path_espd     = path_geral + "/graphics/objeto/espada.png"
path_fog_1    = path_geral + "/graphics/objeto/fog/1.png"
path_fog_2    = path_geral + "/graphics/objeto/fog/2.png"
path_fog_3    = path_geral + "/graphics/objeto/fog/3.png"
path_fog_4    = path_geral + "/graphics/objeto/fog/4.png"
path_grama_1  = path_geral + "/graphics/objeto/grama/11.png"
path_grama_2  = path_geral + "/graphics/objeto/grama/22.png"
path_grama_3  = path_geral + "/graphics/objeto/grama/33.png"
path_grama_4  = path_geral + "/graphics/objeto/grama/44.png"
path_mouse_1  = path_geral + "/graphics/objeto/mouse/1.png"
path_mouse_2  = path_geral + "/graphics/objeto/mouse/2.png"
path_mouse_3  = path_geral + "/graphics/objeto/mouse/3.png"
path_mouse_4  = path_geral + "/graphics/objeto/mouse/4.png"
path_mouse_5  = path_geral + "/graphics/objeto/mouse/5.png"
path_mouse_6  = path_geral + "/graphics/objeto/mouse/6.png"
path_vida     = path_geral + "/graphics/vida/1.png"

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.image.fill("blue")
		self.rect  = self.image.get_rect(topleft = pos)

	def update(self,x_shift):
		self.rect.x += x_shift	

class Mpblock(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.image.fill("blue")
		self.rect  = self.image.get_rect(topleft = pos)

	def update(self, x_shift):
		self.rect.x += x_shift
		pass			

class Tpblock(pygame.sprite.Sprite):
	#Vai pegar uma posição, um tamanho e criar um retangulo
	def __init__(self, pos, size):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.image.fill("red")
		self.rect  = self.image.get_rect(topleft = pos)

	#Vai movimentar os sprites pra parecer uma camera	
	def update(self,x_shift):
		self.rect.x += x_shift		

class Rock(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		self.image = pygame.image.load(path_rock)
		self.image = pygame.transform.scale(self.image, (tile_size, tile_size))	
		self.rect  = self.image.get_rect(topleft = pos)

	def update(self,x_shift):
		self.rect.x += x_shift		

class Prd1(pygame.sprite.Sprite):
	#Vai pegar uma posição, um tamanho e criar um retangulo
	def __init__(self, pos):
		super().__init__()
		size1 = randint(300, 600)
		size2 = randint(800, 1080)
		cor   = randint(0,4)
		self.image = pygame.Surface((size1,size2))
		self.image.fill((randint(0,15),randint(0,15),randint(0,15)))	
		self.rect  = self.image.get_rect(topleft = pos)

	#Vai movimentar os sprites pra parecer uma camera	
	def update(self,x_shift):
		self.rect.x += (10*x_shift)//randint(10,25) #parallax

class Barl(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.image.load(path_barl)
		self.rect  = self.image.get_rect(bottomleft = pos)

	def update(self,x_shift):
		self.rect.x += x_shift		

class Post(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.image.load(path_post)
		self.rect  = self.image.get_rect(bottomleft = pos)
	
	def update(self,x_shift):
		self.rect.x += x_shift		

class Cabn(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.image.load(path_cabn)
		self.rect  = self.image.get_rect(bottomleft = pos)
	
	def update(self,x_shift):
		self.rect.x += x_shift	

class Arv1(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.image.load(path_arv1)
		self.rect  = self.image.get_rect(midbottom = pos)
		num = randint(0,1)
		if num%2==0:
			pass
		else:
			self.image = pygame.transform.flip(self.image, True, False)	

	def update(self,x_shift):
		self.rect.x += x_shift	

class Arv2(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.image.load(path_arv2)
		self.rect  = self.image.get_rect(midbottom = pos)

	def update(self,x_shift):
		self.rect.x += x_shift		

class Arv3(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.image.load(path_arv3)
		self.rect  = self.image.get_rect(midbottom = pos)

	def update(self,x_shift):
		self.rect.x += x_shift	

class Arvf(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.image.load(path_arvf)
		self.rect  = self.image.get_rect(midbottom = pos)

	def update(self,x_shift):
		self.rect.x += x_shift			

class Espd(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.image.load(path_espd)
		self.rect  = self.image.get_rect(midbottom = pos)

	def update(self,x_shift):
		self.rect.x += x_shift			

class Fog(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		img1 = pygame.image.load(path_fog_1)
		img2 = pygame.image.load(path_fog_2)
		img3 = pygame.image.load(path_fog_3)
		img4 = pygame.image.load(path_fog_4)
		self.animations = []
		self.animations.append(img1)
		self.animations.append(img2)
		self.animations.append(img3)
		self.animations.append(img4)

		self.animation_index = 0
		self.image = self.animations[int(self.animation_index)]
		self.rect  = self.image.get_rect(bottomleft = pos)

	def animation(self):
		self.image = self.animations[int(self.animation_index)]
		self.animation_index += 0.2
		if 	self.animation_index >= 3:
			self.animation_index = 0

	def update(self,x_shift):
		self.animation()
		self.rect.x += x_shift	

class Grass(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		img1 = pygame.image.load(path_grama_1)
		img2 = pygame.image.load(path_grama_2)
		img3 = pygame.image.load(path_grama_3)
		img4 = pygame.image.load(path_grama_4)
		self.animations = []
		self.animations.append(img1)
		self.animations.append(img2)
		self.animations.append(img3)
		self.animations.append(img4)

		self.animation_index = 0
		self.image = self.animations[int(self.animation_index)]
		self.rect  = self.image.get_rect(bottomleft = pos)

	def animation(self):
		self.image = self.animations[int(self.animation_index)]
		self.animation_index += 0.1
		if 	self.animation_index >= 3:
			self.animation_index = 0

	def update(self,x_shift):
		self.animation()
		self.rect.x += x_shift				

class Mouse(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		img1 = pygame.image.load(path_mouse_1)
		img2 = pygame.image.load(path_mouse_2)
		img3 = pygame.image.load(path_mouse_3)
		img4 = pygame.image.load(path_mouse_4)
		img5 = pygame.image.load(path_mouse_5)
		img6 = pygame.image.load(path_mouse_6)
		self.animations = []
		self.animations.append(img1)
		self.animations.append(img2)
		self.animations.append(img3)
		self.animations.append(img4)
		self.animations.append(img5)
		self.animations.append(img6)


		self.animation_index = 0
		self.image = self.animations[int(self.animation_index)]
		self.rect  = self.image.get_rect(center = pos)								
	
	def animation(self):
		self.image = self.animations[int(self.animation_index)]
		self.animation_index += 0.03
		if 	self.animation_index >= 6:
			self.animation_index = 0

	def update(self):
		self.animation()

class Vida(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()	
		self.image = pygame.image.load(path_vida)
		self.rect  = self.image.get_rect(midbottom = pos)

	def update(self): #Pro __init__ rodar eu tenho q chamar alguma função
		pass	      #Por conveniencia, chamei o update mesmo

