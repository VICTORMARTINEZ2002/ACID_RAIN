import pygame, sys
from random import randint
from pyvidplayer2 import Video
from pygame import mixer

from tiles import Tile, Rock, Tpblock
from tiles import Barl, Post, Cabn, Espd
from tiles import Fog, Grass
from tiles import Arv1, Arv2, Arv3, Arvf 
from tiles import Prd1
from tiles import Vida
from configurações import level_map, tile_size, screen_width, screen_height
from player import Player
from acid   import Acid

class Level:
	def __init__(self,level_data,surface):
		# level setup
		self.display_surface = surface
		self.setup_level(level_data)
		self.world_shift = 0
		self.chuva_density = 30

		self.remover_vida = False
		self.vidas_inicial = 6
		self.cont_aumenta_vida = 0
		self.vidas_restant = self.vidas_inicial
		self.invulneravel = 0
		self.morto = False
		self.avançar = False

	# deveria corrigir bug da colisão/dash, n corrigiu, mas eu deixei pq mal n faz(além de pesar no jogo)	
		self.bck_cld_righ = [[],[],[],[],[],[]]
		self.bck_cld_left = [[],[],[],[],[],[]]
		self.bck_cld_up   = [[],[],[],[],[],[]]
		self.bck_cld_down = [[],[],[],[],[],[]]

	#iniciando os corações do player	
		self.colocar_todos_os_corações()

	def setup_level(self, layout):
		#Vai pegar uma mapa na forma de lista de string, "salvar como desenho" e agrupar todo mundo em um grupo
		self.tiles  = pygame.sprite.Group()
		self.tpiles = pygame.sprite.Group()
		self.objts  = pygame.sprite.Group() #Stop Acido, acima tiles
		self.objtsI = pygame.sprite.Group() #pass Acido, abaixo tiles
		self.objtsA = pygame.sprite.Group() #pass acido, abaixo tiles
		self.objtsP = pygame.sprite.Group() #pass acido, abaixo tiles
		self.acid   = pygame.sprite.Group()
		self.fog    = pygame.sprite.GroupSingle() #frente do player
		self.grama  = pygame.sprite.Group() #frente do player
		self.player = pygame.sprite.GroupSingle()

		for row_index,row in enumerate(layout):
			for col_index,cell in enumerate(row):
			#blocos              
				x = col_index * tile_size
				y = row_index * tile_size
				if cell == "R":	#bloco azul
					tile = Tile((x,y),tile_size)
					self.tiles.add(tile)
				if cell == "X": #bloco mine
					rock = Rock((x,y), tile_size)
					self.tiles.add(rock)
				if cell == "N":
					tp = Tpblock((x,y), tile_size)
					self.tpiles.add(tp)	
			#objetos de decoração
				if cell == "B": #barril
					x = (col_index) * (tile_size)
					y = (row_index+1) * (tile_size) +13
					barl = Barl((x,y))
					self.objts.add(barl)
				if cell == "I": #poste
					x = (col_index) * (tile_size)
					y = (row_index+1) * (tile_size) 
					poste = Post((x,y))
					self.objtsI.add(poste)
				if cell == "C": #cabana
					x = (col_index) * (tile_size)
					y = (row_index+1) * (tile_size) + 5 
					cabana = Cabn((x,y))
					self.objts.add(cabana)
				if cell == "E": #espada guts
					x = (col_index) * (tile_size)
					y = (row_index+2) * (tile_size) + 15
					espada = Espd((x,y))
					self.objtsA.add(espada)
				if cell == "F": #fogueira
					x = (col_index) * (tile_size)
					y = (row_index+1) * (tile_size) + 25
					fog = Fog((x,y))
					self.fog.add(fog)
				if cell == "G": #grama
					x = (col_index) * (tile_size)
					y = (row_index+1) * (tile_size)
					grama = Grass((x,y))
					self.grama.add(grama)				
			#parallax            
				if cell == "V": #prd1
					x = (col_index) * (tile_size)
					y = (row_index+1) * (tile_size) + 5 
					predio = Prd1((x,y))
					self.objtsP.add(predio)	
			#ARVORES:            
				if cell == "T": #arvore 1
					x = (col_index) * (tile_size)
					y = (row_index+2) * (tile_size)
					arvore = Arv1((x,y))
					self.objtsI.add(arvore)
				if cell == "Y": #arvore 2
					x = (col_index) * (tile_size)
					y = (row_index+1) * (tile_size) + 15
					arvore = Arv2((x,y))
					self.objtsI.add(arvore)
				if cell == "U": #arvore 2
					x = (col_index) * (tile_size)
					y = (row_index+1) * (tile_size)
					arvore = Arv3((x,y))
					self.objtsI.add(arvore)		
				if cell == "8": #arvore viva
					x = (col_index) * (tile_size)
					y = (row_index+1) * (tile_size) + 30
					arvore = Arvf((x,y))
					self.objts.add(arvore)
			#player:             
				if cell == "P": #player
					x = col_index * tile_size
					y = row_index * tile_size
					player_sprite = Player((x,y))
					self.player.add(player_sprite)

	def scroll_x(self):
		player         = self.player.sprite
		player_x       = self.player.sprite.collision_rect.centerx
		direction_x    = self.player.sprite.direction.x
		player_running = self.player.sprite.player_running
		player_dashing = self.player.sprite.player_dashing
			
		if player_x < screen_width*(29/60) and direction_x < 0:
			player.speed = 0
			if player_running:
				self.world_shift = +20
			elif player_dashing:
				self.world_shift = +35	
			else:
				self.world_shift = +8
		elif player_x > screen_width*(31/60) and direction_x > 0:
			player.speed = 0
			if player_running:
				self.world_shift = -20
			elif player_dashing:
				self.world_shift = -35		
			else:
				self.world_shift = -8			
		else:
			self.world_shift = 0
			if player_running:
				player.speed = +20
			elif player_dashing:
				self.world_shift = +35		
			else:
				player.speed = +8	

#ACID:
	def colide_delete(self): #acido
		for sprite in self.acid:
			for tile in self.tiles:
				if sprite.rect.colliderect(tile.rect):
					self.acid.remove(sprite)
			for player in self.player:
				if sprite.rect.colliderect(player.collision_rect):
					self.acid.remove(sprite)
					if self.invulneravel<=0:
						self.remover_vida = True		
			for objt in self.objts:
				if sprite.rect.colliderect(objt.rect):
					self.acid.remove(sprite)
			if sprite.rect.y > 1080:
				self.acid.remove(sprite)

	def ger_random(self): #acido
		x= randint(0, 1920) 
		#y= randint(0, 75)
		self.num = randint(1, self.chuva_density)
		if self.num <= 3:
			acid_sprite = Acid((x,0))
			self.acid.add(acid_sprite)
			for sprite in self.acid:
				for tile in self.tiles:
					if sprite.rect.colliderect(tile.rect):
						self.acid.remove(sprite)	

#Player
	def horizontal_movement_collision(self):
		player = self.player.sprite
		player.collision_rect.x += (player.direction.x*player.speed) #A função collisão engloba o que antes era movimentação do player
		
		for sprite in self.tpiles.sprites():
			if sprite.rect.colliderect(player.collision_rect):
				self.avançar = True	

		if player.facing_right==False:		
			for sprite in self.tiles.sprites():
				if sprite.rect.colliderect(player.collision_rect):
					self.world_shift = 0
					for grupo in self.bck_cld_righ:
						if sprite not in grupo:
							if sprite.rect.centerx > player.collision_rect.centerx:
								pass
							else:
								if player.player_dashing:
									player.cont_dash_d = -1  						    
									self.player.sprite.player_dashing = False           
									player.cont_dash_p = 40
									player.collision_rect.left = sprite.rect.right + 0
								else:	
									player.collision_rect.left = sprite.rect.right
							self.bck_cld_left[5].append(sprite)
			self.bck_cld_left[0]=self.bck_cld_left[1]
			self.bck_cld_left[1]=self.bck_cld_left[2]
			self.bck_cld_left[2]=self.bck_cld_left[3]
			self.bck_cld_left[3]=self.bck_cld_left[4]
			self.bck_cld_left[4]=self.bck_cld_left[5]
			self.bck_cld_left[5]=[]

		elif player.facing_right:	
			for sprite in self.tiles.sprites():	
				if sprite.rect.colliderect(player.collision_rect):
					self.world_shift = 0 # eu fiz tanta mais tanta coisa p resolver o bug da colisão e era só colocar essa
					for grupo in self.bck_cld_left:
						if sprite not in grupo:
							if sprite.rect.centerx < player.collision_rect.centerx:
								pass
							else:	
								if player.player_dashing:
									player.cont_dash_d = -1                             
									self.player.sprite.player_dashing = False
									player.cont_dash_p = 40				
									player.collision_rect.right = sprite.rect.left - 100
								else:
									player.collision_rect.right = sprite.rect.left	
						self.bck_cld_righ[5].append(sprite)
			self.bck_cld_righ[0]=self.bck_cld_righ[1]
			self.bck_cld_righ[1]=self.bck_cld_righ[2]
			self.bck_cld_righ[2]=self.bck_cld_righ[3]
			self.bck_cld_righ[3]=self.bck_cld_righ[4]
			self.bck_cld_left[5]=[]

	def vertical_movement_collision(self):
		player = self.player.sprite
		player.apply_gravity()			

		if player.cont_dash_d == -1:
			pass
		else:
			if player.direction.y>0:
				for sprite in self.tiles.sprites():
					if sprite.rect.colliderect(player.collision_rect):
						for grupo in self.bck_cld_up:
							if sprite not in grupo:
								if sprite.rect.centery < player.collision_rect.centery:
									pass
								else:	
									player.collision_rect.bottom = sprite.rect.top
									player.direction.y = 0
									player.on_ground   = True
									player.fez_segundo_dash = False
			elif player.direction.y<0:
				for sprite in self.tiles.sprites():
					if sprite.rect.colliderect(player.collision_rect):	
						for grupo in self.bck_cld_down:
							if sprite not in grupo:
								if sprite.rect.centery > player.collision_rect.centery:
									pass
								else:					
									player.collision_rect.top    = sprite.rect.bottom
									player.direction.y = 0
									player.on_ceiling  = True

		if player.on_ground and player.direction.y<0 or player.direction.y>=1: #esse 1 "é da gravidade
			player.on_ground = False

		if player.collision_rect.y > 2100:
			self.morto = True	

#vida do player:		
	def colocar_todos_os_corações(self):
		self.life = pygame.sprite.Group()
		for i in range(0, self.vidas_restant):
			y = 100
			x = 70*(1+i)
			self.img_vp = Vida((x,y))
			self.life.add(self.img_vp)

	def contar_vida_player(self):
		if self.invulneravel<=0 and self.remover_vida:
			self.remover_vida = False
			self.vidas_restant -= 1
			self.life.empty()
			self.colocar_todos_os_corações()
			self.invulneravel = 90
			if self.vidas_restant<=0:
				self.morto = True
		self.aumentar_vida_player()	

	def aumentar_vida_player(self):
		player = self.player.sprite
		if self.cont_aumenta_vida <= 0:
			self.cont_aumenta_vida = 45
			for sprite in self.fog.sprites():
				if sprite.rect.colliderect(player.collision_rect):
					self.invulneravel = 90
					self.vidas_restant += 1
					if self.vidas_restant >6:
						self.vidas_restant= 6
					self.life.empty()
					self.colocar_todos_os_corações()

#run:
	def run(self):
	#contador
		self.invulneravel -= 1
		self.invulneravel = max(self.invulneravel, 0)
		self.cont_aumenta_vida -= 1
		self.cont_aumenta_vida = max(self.cont_aumenta_vida, 0)

	#atualizar objetos
		self.player.update()
		self.tiles.update(self.world_shift)
		self.tpiles.update(self.world_shift)
		self.objts.update(self.world_shift)
		self.objtsI.update(self.world_shift)
		self.objtsA.update(self.world_shift)
		self.objtsP.update(self.world_shift)
		self.fog.update(self.world_shift)
		self.grama.update(self.world_shift)
		self.acid.update(int(self.world_shift*randint(9,12)//10))
		self.life.update()   #Nem precisa atualizar, mas essa função fazer rodar o __init__))

	#acido geração e colisão	
		self.colide_delete()
		self.ger_random()

	#São desenhados abaixo das tiles
		self.objtsA.draw(self.display_surface)
		self.objtsP.draw(self.display_surface)

		self.tiles.draw(self.display_surface)#desenha todo mundo do grupo tiles na tela(faz o mapa)
		self.tpiles.draw(self.display_surface)

	#São desenhados em cima das tiles		
		self.objts.draw(self.display_surface)
		self.objtsI.draw(self.display_surface)
		self.acid.draw(self.display_surface)

	#mundo camera	
		self.scroll_x()	

	# player
		self.horizontal_movement_collision()
		self.vertical_movement_collision()
		

		self.player.draw(self.display_surface) #desenha o unico sprite do GroupSingle player na tela
		self.contar_vida_player()
		self.life.draw(self.display_surface)

		self.grama.draw(self.display_surface)
		self.fog.draw(self.display_surface)

			

		