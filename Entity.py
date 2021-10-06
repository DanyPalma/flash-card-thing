# Entity code here #

import Utils as u

class Entity:
	def __init__(self, name, x, y, pg):
		self.x = x
		self.y = y
		self.velx = 0
		self.vely = 0
		self.sprite = u.loadasset(name, pg)

	def render(self, display):
		display.blit(self.sprite, (self.x, self.y))

