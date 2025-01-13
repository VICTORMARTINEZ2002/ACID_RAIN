import pygame
from tiles import Mpblock
from level import Level
from configurações import level_map, level_map2

class Mapa:
	def __init__(self,mapa_data,surface):
		self.display_surface = surface
		self.tile_size = 16
		self.configurar_map(mapa_data)

	def configurar_map(self, layout):
		self.tiles  = pygame.sprite.Group()
		self.icone = pygame.sprite.GroupSingle()

		for row_index,row in enumerate(layout):
			for col_index,cell in enumerate(row):
				x = col_index * self.tile_size
				y = 300 + row_index * self.tile_size
				if cell == "R":	#bloco azul
					tile = Mpblock((x,y), self.tile_size)
					self.tiles.add(tile)
				if cell == "P":
					pass

	def atualizar_mapa(deltax):
		self.tiles.update(self.world_shift)				
						
	def run(self):
		#self.contador -= 1
		#self.contador = max(self.contador, 0)

		self.tiles.update()
		self.tiles.draw(self.display_surface)				

