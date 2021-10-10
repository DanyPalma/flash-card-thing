# Textbox code here #

import Utils as u

class Textbox:
	def __init__(self, pg, x, y, w, h, text, color, fontsize):
		self.text = text
		self.hitbox = pg.Rect(x, y, w, h)
		self.color = color
		font = pg.font.Font(None, fontsize) 
		self.sur = font.render(text, True, color)
		self.active = False

	def render(self, pygame, display):
		pygame.draw.rect(display, self.color, self.hitbox, 1)
		display.blit(self.sur, self.hitbox)
		
	def istouching(self, hitbox2):
		return hitbox2.colliderect(self.hitbox) 

	def toggle(self):
		#self.color = (0, 255, 0)
		self.active = not self.active

