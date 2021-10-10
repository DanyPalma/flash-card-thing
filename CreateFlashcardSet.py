# Createset Code #

import sys
import Utils as u
import Textbox as tb

entities = [] 
pressed = None
boxes = []
cards = []
currentcard = 0


class Card:
	def __init__(self, front, back):
		self.front = front
		self.back = back

	def setfront(self, newfront):
		self.front = newfront
		
	def setback(self, newback):
		self.back = newback

	def getfront(self):
		return self.front

	def getback(self):
		return self.back


def done():
	try: 
		temp = cards[currentcard]
	except:
		create()

	# create a json file containing everything #
	if boxes[0].text == '':
		return
	f = open(f'{boxes[0].text}.json', 'w')
	f.write('[\n')
	for x, card in enumerate(cards):
		print(x)
		f.write('\t{ "Front" : "' + card.front + '",\n')	
		if x == len(cards)-1:
			f.write('\t  "Back" : "' + card.back + '" }\n\n')	
		else:
			f.write('\t  "Back" : "' + card.back + '" },\n\n')	

	f.write(']')
	return 1

	
def right():
	global currentcard
	try: 
		temp = cards[currentcard]
	except:
		create()

	currentcard += 1
	try: 
		boxes[1].text = cards[currentcard].front
		boxes[2].text = cards[currentcard].back
	except:
		boxes[1].text = ''
		boxes[2].text = ''


def left():
	global currentcard
	if currentcard == 0:
		return
	try:
		temp = cards[currentcard]
	except:
		create()

	currentcard -= 1
	boxes[1].text = cards[currentcard].front
	boxes[2].text = cards[currentcard].back


def create():
	global cards
	newcard = Card(boxes[1].text, boxes[2].text)
	cards.append(newcard)


def delete():
	global cards
	cards.pop(currentcard)
	boxes[1].text = cards[currentcard].front
	boxes[2].text = cards[currentcard].back


def init(pg, plr, ent):
	global entities
	global boxes
	entities.append(ent.Entity('blank', 841, 25, 248, 72, pg, done))
	entities.append(ent.Entity('blank', 448, 576, 128, 128, pg, None))
	entities.append(ent.Entity('blank', 704, 576, 128, 128, pg, delete))
	entities.append(ent.Entity('blank', 192, 576, 128, 128, pg, left))
	entities.append(ent.Entity('blank', 960, 576, 128, 128, pg, right))

	boxes.append(tb.Textbox(pg, 192, 18, 536, 79, '', (255, 255, 255), 32))
	boxes.append(tb.Textbox(pg, 64, 192, 512, 320, '', (255, 255, 255), 32))
	boxes.append(tb.Textbox(pg, 704, 192, 512, 320, '', (255, 255, 255), 32))


def update(pygame, display, deltatime, cs):
	# tick
	pressed = pygame.key.get_pressed()
	events = pygame.event.get()
	for event in events:
		if event.type == 256:
			pygame.quit()
			sys.exit()

	# render
	display.fill((19, 27, 35))
	display.blit(u.ASSETS[4], (0, 0))

	#sur = lolfont.render(f'Card {currentcard+1} out of {len(cards)}', True, (255, 255, 255))

	# fix this. yuck #
	for box in boxes:
		box.render(pygame, display)
		if box.active:
			for event in events:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE:
						box.text = box.text[0:-1]
					else:
						box.text += event.unicode
		if pygame.mouse.get_pressed() == (1, 0, 0):
			box.turnoff()
			mpos = pygame.mouse.get_pos()
			temp = pygame.Rect(mpos[0], mpos[1], 10, 10)
			if box.istouching(temp):
				box.turnon()
	
	for e in entities:
		for event in events:
			if event.type == pygame.MOUSEBUTTONUP:
				mpos = pygame.mouse.get_pos()
				temp = pygame.Rect(mpos[0], mpos[1], 10, 10)
				if e.istouching(temp):
					if e.activate() == 1:
						return 2

	return cs


