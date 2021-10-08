# Game Code #

import sys
import Utils as u

entities = [] 
player = None
pressed = None

def init(pg, plr, ent):
	global player
	global entities
	player = plr.Player(100, 100, pg)
	boxa = ent.Entity('blank', 833, 56, 294, 249, pg)
	boxb = ent.Entity('blank', 800, 396, 295, 242, pg)
	entities.append(boxa)
	entities.append(boxb)


def render(display, cs):
	display.fill((19, 27, 35))
	display.blit(u.ASSETS[2], (0, 0))
	for e in entities:
		e.render(display)
		if e.istouching(player.hitbox):
			display.blit(u.ASSETS[0], (player.x, player.y-64))
			if pressed[101]:
				return 0 
	player.render(display)
	return cs


def tick(pygame, deltatime):
	global pressed
	pressed = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == 256:
			pygame.quit()
			sys.exit()
	player.update(deltatime, pressed)
	return 0;

