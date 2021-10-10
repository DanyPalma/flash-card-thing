# Createset Code #

import sys
import Utils as u
import Textbox as tb

entities = [] 
pressed = None
boxes = []

def init(pg, plr, ent):
	global entities
	global boxes
	entities.append(ent.Entity('blank', 841, 25, 248, 72, pg, None))
	entities.append(ent.Entity('blank', 448, 576, 128, 128, pg, None))
	entities.append(ent.Entity('blank', 704, 576, 128, 128, pg, None))
	entities.append(ent.Entity('blank', 192, 576, 128, 128, pg, None))
	entities.append(ent.Entity('blank', 960, 576, 128, 128, pg, None))

	boxes.append(tb.Textbox(pg, 192, 18, 536, 79, 'fart', (255, 255, 255), 32))
	boxes.append(tb.Textbox(pg, 64, 192, 512, 320, 'fart2', (255, 255, 255), 32))
	boxes.append(tb.Textbox(pg, 704, 192, 512, 320, 'fart3', (255, 255, 255), 32))


def update(pygame, display, deltatime, cs):
	# tick
	global text
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_BACKSPACE]:
		pass
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN:
				pass
		if event.type == 256:
			pygame.quit()
			sys.exit()

	# render
	display.fill((19, 27, 35))
	display.blit(u.ASSETS[4], (0, 0))

	for box in boxes:
		box.render(pygame, display)
		if pygame.mouse.get_pressed() == (1, 0, 0):
			mpos = pygame.mouse.get_pos()
			temp = pygame.Rect(mpos[0], mpos[1], 10, 10)
			if box.istouching(temp):
				box.toggle()

	return cs


