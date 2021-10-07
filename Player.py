# All player code goes here #

import Utils as u

class Player:
	def __init__(self, x, y, pg):
		self.x = x
		self.y = y
		self.velx = 0
		self.vely = 0
		self.hitbox = pg.Rect(x, y, 64, 64)
		self.sprite = u.loadasset('tempcharacter', pg)

	def update(self, dt, pressed):
		# this is horrid #
		speed = 0.2
		maxspeed = 0.5
		drag = 0.05

		if pressed[119] and self.vely > -maxspeed:
			self.vely -= speed
		if pressed[115] and self.vely < maxspeed:
			self.vely += speed
		if pressed[97] and self.velx > -maxspeed:
			self.velx -= speed
		if pressed[100] and self.velx < maxspeed:
			self.velx += speed

		self.y += dt * self.vely
		self.x += dt * self.velx

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

		# Wrap around the screen #
		if self.x > 1280:
			self.x = -64 
		elif self.x < -64:
			self.x = 1280

		if self.y > 720:
			self.y = -64 
		elif self.y < -64:
			self.y = 720

		self.hitbox.update(self.x, self.y, 64, 64)


	def render(self, display):
		display.blit(self.sprite, (self.x, self.y))

