# Flashcard Code #

import sys
import Utils as u

entities = [] 
pressed = None


def init(pg, plr, ent):
	global entities
	addset = ent.Entity('blank', 1024, 8, 107, 52, pg, None)
	entities.append(addset)


def update(pygame, display, deltatime, cs):
	# tick
	global pressed
	pressed = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == 256:
			pygame.quit()
			sys.exit()

	# render
	display.fill((19, 27, 35))
	display.blit(u.ASSETS[2], (0, 0))
	for e in entities:
		e.render(display)

	if pygame.mouse.get_pressed() == (1, 0, 0):
		e = entities[0]
		mpos = pygame.mouse.get_pos()
		temp = pygame.Rect(mpos[0], mpos[1], 10, 10)
		if e.istouching(temp):
			return 3

	return cs


