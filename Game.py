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
	boxa = ent.Entity('blank', 833, 56, 294, 249, pg, None)
	boxb = ent.Entity('blank', 800, 396, 295, 242, pg, None)
	entities.append(boxa)
	entities.append(boxb)
	print('game init')


def render(display, deltatime, cs):
	# tick
	global pressed
	pressed = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == 256:
			pygame.quit()
			sys.exit()
	player.update(deltatime, pressed)

	# render
	display.fill((19, 27, 35))
	display.blit(u.ASSETS[1], (0, 0))
	for e in entities:
		e.render(display)
		if e.istouching(player.hitbox):
			display.blit(u.ASSETS[0], (player.x, player.y-64))
			if pressed[101]:
				return 2 
	player.render(display)
	if player.y < 0:
		return 1
	return cs


