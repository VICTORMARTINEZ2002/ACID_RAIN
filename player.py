import pygame, os
from support import import_folder

from configurações import screen_height

class Player(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
	#path geral
		self.path_geral      = os.getcwd()
		self.path_dash_sound = self.path_geral + "/graphics/video/dash.wav"
		self.path_pulo_sound = self.path_geral + "/graphics/video/pulo.wav"

	#sprite	
		self.import_character_assets()
		self.frame_index = 0
		self.animation_speed = 0.15
		self.image = self.animations["idle"][self.frame_index]
		self.rect = self.image.get_rect(topleft = pos)

	#audios
		pygame.mixer.init()
		self.dash__sound = pygame.mixer.Sound(self.path_dash_sound)
		pygame.mixer.Sound.set_volume(self.dash__sound, 0.3)
		self.pulo__sound = pygame.mixer.Sound(self.path_pulo_sound)
		pygame.mixer.Sound.set_volume(self.pulo__sound, 0.3)
		

	# player movement
		self.direction = pygame.math.Vector2(0,0)
		self.speed      =   12
		self.gravity    = 0.4
		self.jump_speed = -16

	# Gambinho
		self.str1, self.str2 = str(self.rect.topleft).split(",")
		self.str1 = self.str1[1:]
		self.str2 = self.str2[1:]
		self.str2 = self.str2[:1]
		self.str1 = int(self.str1)
		self.str2 = int(self.str2)

		self.collision_rect = pygame.Rect(self.str1, self.str2-20, 115, 170)

 	#Contadores
		self.cont_pulo = 0
		self.cont_dash_d = 0 #duração do dash
		self.cont_dash_c = 0 #tirar a merda do problema na
		self.cont_dash_p = 0 #habil a fazer novo dash

		self.delay_cam = 120

	# player status
		self.status  = "idle"
		self.fez_segundo_pulo = False
		self.fez_segundo_dash = False
		self.facing_right   = True
		self.player_running = False
		self.player_dashing = False
		self.on_ground      = False
		self.on_ceiling     = False

	def import_character_assets(self):
		character_path = self.path_geral + "/graphics/character/"
		self.animations = {"idle":[], "run":[], "dash":[], "jump(cres)":[], "jump(desc)":[], "land":[], "dead":[], "walljump": []}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)	

	def animate(self):
		animation = self.animations[self.status]

		#loop over frame index
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		#flip the image basing on facing		
		if self.facing_right:
			self.image = animation[int(self.frame_index)]
			self.rect.bottomleft = self.collision_rect.bottomleft		
		else:
			self.image = pygame.transform.flip(animation[int(self.frame_index)], True, False)
			self.rect.bottomright = self.collision_rect.bottomright #aqui #########

		self.rect = self.image.get_rect(midbottom = self.rect.midbottom)	

	def get_input(self):
		keys = pygame.key.get_pressed()

	#respawn	
		if keys[pygame.K_p]:
			self.collision_rect = pygame.Rect(self.str1, self.str2 ,120, 190)
			self.direction.y = 0

	#dash	
		if self.cont_dash_p>0:					 #Estar habil a fazer o prox dash?
			pass
		else:		
			if keys[pygame.K_c]:
				if self.on_ground:
					self.dash()
					self.fez_segundo_dash = False
					self.cont_dash_d = 15
					self.cont_dash_p = 30
				else:
					if self.fez_segundo_dash==False:
						self.dash()
						self.fez_segundo_dash = True
						self.cont_dash_d = 15
						self.cont_dash_p = 30	

	#move/run			
		if self.cont_dash_d<=0:					 #Não estar no meio de um dash
			self.player_dashing = False

			if  keys[pygame.K_RIGHT]:
				self.direction.x = +1
				self.facing_right = True

				if keys[pygame.K_LSHIFT]:
					self.player_running = True
					self.speed = 20
				else:	
					self.player_running = False
					self.speed = 8
			elif keys[pygame.K_LEFT]:
				self.direction.x = -1
				self.facing_right = False
				if keys[pygame.K_LSHIFT]:
					self.player_running = True
					self.speed = 20
				else:
					self.player_running = False
					self.speed = 8	
			else:
				self.direction.x = 0
				self.player_running = False	

			#pulo	
			if keys[pygame.K_z] and self.on_ground:
				self.jump()
				self.pulo__sound.play()
				self.fez_segundo_pulo = False
				self.cont_pulo = 20
			elif keys[pygame.K_z] and not self.fez_segundo_pulo and self.cont_pulo<=0:
				self.jump()
				self.fez_segundo_pulo = True

	def get_status(self):
		if   self.player_dashing:
			self.status = "dash"
		elif self.direction.y<0:
			self.status = "jump(cres)"
		elif self.direction.y> 2*self.gravity: # descendo mais do que o que o player desce só por colidir com o bloco
			self.status = "jump(desc)"
		else:
			if self.direction.x != 0:
				self.status = "run"
			else:
				self.status = "idle"					

	def apply_gravity(self):
		if self.player_dashing==False:
			self.direction.y += self.gravity
			self.collision_rect.y += self.direction.y		

	def jump(self):
		self.direction.y = self.jump_speed

	def dash(self):
		self.player_running  = False
		self.player_dashing  = True
		self.direction.y = 0

		self.speed = 35
		if self.facing_right:
			self.direction.x = +1
		else:
			self.direction.x = -1
		self.dash__sound.play()
			

	def update(self):
		self.cont_pulo -= 1
		self.cont_pulo = max(self.cont_pulo, 0)

		self.cont_dash_d -= 1
		self.cont_dash_d = max(self.cont_dash_d, 0)
		self.cont_dash_p -= 1
		self.cont_dash_p = max(self.cont_dash_p, 0)

		self.delay_cam -= 1
		self.delay_cam = max(self.delay_cam, 0)


		self.get_input()
		self.get_status()
		self.animate() 
			