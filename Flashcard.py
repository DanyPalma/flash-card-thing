# Flashcard Code #

import sys
import Utils as u
from os import listdir

entities = [] 
pressed = None
cardlist = []

def backbtn():
	return 1

def createsetbtn():
	return 3


def init(pg, plr, ent):
	global entities
	global cardlist
	addset = ent.Entity('blank', 1024, 8, 107, 52, pg, createsetbtn)
	back = ent.Entity('blank', 104, 7, 187, 59, pg, backbtn)
	entities.append(addset)
	entities.append(back)
	files = listdir(sys.path[0])
	cardlist = [f for f in files if f.__contains__('.json')]


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
		if pygame.mouse.get_pressed() == (1, 0, 0):
			mpos = pygame.mouse.get_pos()
			temp = pygame.Rect(mpos[0], mpos[1], 10, 10)
			if e.istouching(temp):
				return e.activate()

	return cs


