# Flashcard Code #

import sys
import Utils as u
from os import listdir

entities = [] 
pressed = None
cards = []
boxes = []

def init(pg, plr, ent):
	global entities
	global boxes
	global cards
	addset = ent.Entity('blank', 1024, 8, 107, 52, pg, lambda : 3)
	back = ent.Entity('blank', 104, 7, 187, 59, pg, lambda : 1)
	entities.append(addset)
	entities.append(back)
	files = listdir(sys.path[0])
	cardlist = [f for f in files if f.__contains__('.json')]
	y = 128
	for card in cardlist:
		newcard = ent.Entity('card', 128, y, 1024, 128, pg, None)
		text = u.Textbox(pg, 192, y+32, 320, 64, card[0:-5], (255, 255, 255), 32)	
		boxes.append(text)
		cards.append(newcard)
		y += 192 


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

	for i in range(len(boxes)):
		cards[i].render(display)
		boxes[i].render(pygame, display)

	for e in entities:
		e.render(display)
		if pygame.mouse.get_pressed() == (1, 0, 0):
			mpos = pygame.mouse.get_pos()
			temp = pygame.Rect(mpos[0], mpos[1], 10, 10)
			if e.istouching(temp):
				return e.activate()

	return cs


