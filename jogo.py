#Iniciar com o compilador python, não compilador python"meu"
import pygame, sys, os
from sys import path


dirpath = path[0]
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
	os.chdir(sys._MEIPASS)
	
from random import randint
from pygame import mixer
from pyvidplayer2 import Video 	

from configurações import *
from player import Player
from level  import Level
from tiles  import Mouse
from mapa   import Mapa


pygame.init()
pygame.mixer.init()

#pygame setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Acid Rain")   
clock = pygame.time.Clock()

#att
level = Level(level_map, screen)
mapa  = Mapa(level_map, screen)

#path geral
path_geral           = os.getcwd()
path_vid             = path_geral + "/graphics/video/intro.mp4"
path_enter_sound     = path_geral + "/graphics/video/sound.ogg"
path_morto_sound     = path_geral + "/graphics/video/DED.mp3"
path_game_music      = path_geral + "/graphics/video/game_music.mp3"
path_tela_inicial_bg = path_geral + "/graphics/bg/intro_screen.png"
path_tela_configu_bg = path_geral + "/graphics/bg/configurações.png"
path_tela_fimjogo_bg = path_geral + "/graphics/bg/yd.png"


#variavies audio-visuais
vid = Video(path_vid)
enter_sound = pygame.mixer.Sound(path_enter_sound)
pygame.mixer.Sound.set_volume(enter_sound, 0.5)
morto_sound = pygame.mixer.Sound(path_morto_sound)
pygame.mixer.Sound.set_volume(morto_sound, 0.3)


#detectar a se a msc acabou e fazer loop
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)
game_music  = pygame.mixer.music.load(path_game_music)

#play
tela_inicial_bg = pygame.image.load(path_tela_inicial_bg)
tela_configu_bg = pygame.image.load(path_tela_configu_bg)
tela_fimjogo_bg = pygame.image.load(path_tela_fimjogo_bg)

def intro():
	while True:
		vid.draw(screen, (0,0))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				vid.close()
				enter_sound.play()
				tela_inicial()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					enter_sound.play()
					vid.close()
					tela_inicial()		
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

def tela_inicial():
	screen.blit(tela_inicial_bg, (0,0))
	indicador = pygame.sprite.GroupSingle()

	att = False
	cont = 200
	pos_y_play = 570
	pos_y_conf = 735
	pos_y_exit = 880
	pos_y_curt = pos_y_play
	pos_y_pass = pos_y_curt
	#mouse
	mouse_sprite = Mouse((700,pos_y_curt))
	indicador.add(mouse_sprite)

	#lopp
	while True:		
		cont -= 1
		cont = max(cont, 0)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()
		if cont<=0:	
			if pos_y_curt == 570:
				if keys[pygame.K_RETURN]:
					screen.fill("black")
					enter_sound.play()
					main()
				if keys[pygame.K_UP]:
					pass	
				elif keys[pygame.K_DOWN]:
					cont=5
					pos_y_curt = 735
					att = True	
			elif pos_y_curt == 735:
				if keys[pygame.K_RETURN]:
					screen.fill("black")
					enter_sound.play()
					tela_cinfigurações()
				if keys[pygame.K_UP]:
					cont=5
					pos_y_curt = 570
					att = True		
				elif keys[pygame.K_DOWN]:
					cont=5
					pos_y_curt = 880
					att = True	
			elif pos_y_curt == 880:
				if keys[pygame.K_RETURN]:
					pygame.quit()
					sys.exit()	
				if keys[pygame.K_UP]:
					cont=5
					pos_y_curt = 735
					att = True		
				elif keys[pygame.K_DOWN]:
					pass

		if att:
			screen.blit(tela_inicial_bg, (0,0))
			mouse_sprite.rect.centery = pos_y_curt				
			att = False	

		indicador.update()
		indicador.draw(screen)		
		pygame.display.update()

def tela_inicial2():
	screen.blit(tela_inicial_bg, (0,0))
	indicador = pygame.sprite.GroupSingle()

	att = False
	cont = 200
	pos_y_play = 570
	pos_y_conf = 735
	pos_y_exit = 880
	pos_y_curt = pos_y_play
	pos_y_pass = pos_y_curt

	mouse_sprite = Mouse((700,pos_y_curt))
	indicador.add(mouse_sprite)

	while True:		
		cont -= 1
		cont = max(cont, 0)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()
		if cont<=0:	
			if pos_y_curt == 570:
				if keys[pygame.K_RETURN]:
					screen.fill("black")
					enter_sound.play()
					main2()
				if keys[pygame.K_UP]:
					pass	
				elif keys[pygame.K_DOWN]:
					cont=5
					pos_y_curt = 735
					att = True	
			elif pos_y_curt == 735:
				if keys[pygame.K_RETURN]:
					screen.fill("black")
					enter_sound.play()
					tela_cinfigurações2()
				if keys[pygame.K_UP]:
					cont=5
					pos_y_curt = 570
					att = True		
				elif keys[pygame.K_DOWN]:
					cont=5
					pos_y_curt = 880
					att = True	
			elif pos_y_curt == 880:
				if keys[pygame.K_RETURN]:
					pygame.quit()
					sys.exit()	
				if keys[pygame.K_UP]:
					cont=5
					pos_y_curt = 735
					att = True		
				elif keys[pygame.K_DOWN]:
					pass

		if att:
			screen.blit(tela_inicial_bg, (0,0))
			mouse_sprite.rect.centery = pos_y_curt				
			att = False	
																
		indicador.update()
		indicador.draw(screen)		
		pygame.display.update()
					
def tela_cinfigurações():
	screen.blit(tela_configu_bg, (0,0))
	while True:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			screen.fill("black")
			tela_inicial()	

def tela_cinfigurações2():
	screen.blit(tela_configu_bg, (0,0))
	while True:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			screen.fill("black")
			tela_inicial2()		

def fim_de_jogo():
	pygame.mixer.music.stop()
	morto_sound.play()
	screen.blit(tela_fimjogo_bg, (0,0))
	while True:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE] or keys[pygame.K_RETURN]:
			level.__init__(level_map, screen)
			level.setup_level(level_map)
			level.run()
			screen.fill("black")
			tela_inicial()	

def tela_mapa(): # em desenvolvimento
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_q]:
			main2()		#mudar isso dps pra main2
		mapa.run()
		pygame.display.update()

def pausar(): #em desenvolvimento
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_i]:
			main2()

def main():
	pygame.mixer.music.play(-1)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			screen.fill("black")
			tela_inicial2()
		if keys[pygame.K_TAB]:
			screen.fill("black") #exe
			tela_mapa()
		if keys[pygame.K_o]:
			pausar()		
		screen.fill((40,40,40))
		level.run()
		pygame.display.update()
		clock.tick(FPS)
		if level.morto==True:
			fim_de_jogo()
		if level.avançar==True:
			prox_mapa()
			
def main2():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MUSIC_END:
				pygame.mixer.music.play(-1)	
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			screen.fill("black")
			tela_inicial2()
		if keys[pygame.K_TAB]:
			screen.fill("black") #exe
			tela_mapa()		
		if keys[pygame.K_o]:
			pausar()								
		screen.fill((40,40,40))
		level.run()
		pygame.display.update()
		clock.tick(FPS)
		if level.morto==True:
			fim_de_jogo()
		if level.avançar==True:
			prox_mapa()		

def prox_mapa():
		level.__init__(level_map2, screen)
		level.setup_level(level_map2)
		level.invulneravel = 3000
		level.run()	

intro()