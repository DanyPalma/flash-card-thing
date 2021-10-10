# Entity code here #

import Utils as u

class Entity:
	def __init__(self, name, x, y, w, h, pg, interactfunc):
		self.x = x
		self.y = y
		self.velx = 0
		self.vely = 0
		self.hitbox = pg.Rect(x, y, w, h)
		self.sprite = u.loadasset(name, pg)
		self.activate = interactfunc 

	def render(self, display):
		display.blit(self.sprite, (self.x, self.y))

	def istouching(self, hitbox2):
		return hitbox2.colliderect(self.hitbox) 

