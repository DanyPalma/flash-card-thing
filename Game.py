# Menu Code #

import Utils as u

def render(display, entities, player):
	display.fill((19, 27, 35))
	for e in entities:
		e.render(display)
		if e.istouching(player.hitbox):
			display.blit(u.ASSETS[0], (player.x, player.y-64))
	player.render(display)


def tick():
	print('game update')

