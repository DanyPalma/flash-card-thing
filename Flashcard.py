# Flashcard Code #

import sys
import Utils as u

entities = [] 
pressed = None

def init(pg, plr, ent):
	global entities
	addset = ent.Entity('blank', 1024, 8, 107, 52, pg, None)
	entities.append(addset)


# These are so ugly the render and the tick methods are getting mixed!!!!!! #
def update(pygame, display, deltatime, cs):
	# tick
	global pressed
	pressed = pygame.key.get_pressed()
	mpos = pygame.mouse.get_pos()
	print(mpos[1])
	if pygame.mouse.get_pressed() == (1, 0, 0):
		print('clociek')
	for event in pygame.event.get():
		if event.type == 256:
			pygame.quit()
			sys.exit()

	# render
	display.fill((19, 27, 35))
	display.blit(u.ASSETS[2], (0, 0))
	for e in entities:
		e.render(display)
	return cs


