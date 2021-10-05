# All player code goes here #

import Utils as u

class Player:
	def __init__(self, x, y, pg):
		self.x = x
		self.y = y
		self.velx = 0
		self.vely = 0
		self.sprite = u.loadasset('tempcharacter', pg)

	def update(self, dt):
		# This looks horrible #
		maxspeed = 0.5
		if self.vely > maxspeed:
			self.vely = maxspeed
		elif self.vely < -maxspeed:
			self.vely = -maxspeed
		self.y += dt * self.vely

		if self.velx > maxspeed:
			self.velx = maxspeed
		elif self.velx < -maxspeed:
			self.velx = -maxspeed
		self.x += dt * self.velx

		drag = 0.05
		if self.vely != 0 and abs(self.vely) > 0.0005:
			if self.vely > 0:
				self.vely -= drag
			elif self.vely < 0:
				self.vely += drag
		else:
			self.vely = 0

		if self.velx != 0 and abs(self.velx) > 0.0005:
			if self.velx > 0:
				self.velx -= drag
			elif self.velx < 0:
				self.velx += drag
		else:
			self.velx = 0

		if self.x > 1280:
			self.x = -64 
		elif self.x < -64:
			self.x = 1280

		if self.y > 720:
			self.y = -64 
		elif self.y < -64:
			self.y = 720




	def render(self, display):
		display.blit(self.sprite, (self.x, self.y))

