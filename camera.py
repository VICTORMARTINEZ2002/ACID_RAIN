import pygame
from player import Player

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()

		#camera offset
		self.offset = pygame.math.Vector2()
		self.half_w = self.display_surface.get_size()[0]//2
		self.half_h = self.display_surface.get_size()[1]//2

		#ground
		self.ground_surf = pygame.image.load("C:/Users/VICTOR/Desktop/meuJogo2/graphics/bg/bg.png")
		self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))

	def center_target_camera(self, target):
		self.offset.x = target.rect.centerx - self.half_w
		self.offset.y =	target.rect.centery - self.half_h

	def custom_draw(self, player):
		self.center_target_camera(player)

		#ground
		ground_offset = self.ground_rect.topleft - self.offset
		self.display_surface.blit(self.gound_surf, ground_offset)

		#active elements
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image, offset_pos)






































