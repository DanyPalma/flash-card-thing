# Utilities #

import sys 

ASSETS = []

def loadasset(name, pg):
	asset = pg.image.load(f'{sys.path[0]}/Static/{name}.png').convert()
	asset.set_colorkey((0, 0, 0))
	return asset;

def initassets(pg):
	global ASSETS
	ASSETS.append(loadasset('prompt', pg))
	ASSETS.append(loadasset('menubg', pg))
	ASSETS.append(loadasset('gamebg', pg))
	ASSETS.append(loadasset('test', pg))
	ASSETS.append(loadasset('createcards', pg))

class Textbox:
	def __init__(self, pg, x, y, w, h, text, color, fontsize):
		self.text = text
		self.hitbox = pg.Rect(x, y, w, h)
		self.color = color
		self.font = pg.font.Font(None, fontsize)
		self.active = False

	def render(self, pygame, display):
		sur = self.font.render(self.text, True, self.color)
		pygame.draw.rect(display, self.color, self.hitbox, 1)
		display.blit(sur, self.hitbox)

	def istouching(self, hitbox2):
		return hitbox2.colliderect(self.hitbox)

	def turnon(self):
		self.active = True
		self.color = (0, 255, 0)

	def turnoff(self):
		self.active = False 
		self.color = (255, 0, 0)

