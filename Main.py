#!/usr/bin/env python

import os
import sys
import time
import pygame
from pygame.locals import *


def loadasset(name):
	asset = pygame.image.load(f'{GAMEPATH}/Assets/{name}.png').convert()
	asset.set_colorkey((0, 0, 0)) # removing black bg
	return asset;


def render():
	display.fill(BGCOLOR)
	player.render()

bruh = 0
def tick(deltatime):
	speed = 0.2
	pressed = pygame.key.get_pressed()
	if pressed[K_w]:
		player.vely -= speed 
	if pressed[K_s]:
		player.vely += speed
	if pressed[K_a]:
		player.velx -= speed
	if pressed[K_d]:
		player.velx += speed

	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
			pygame.quit()
			sys.exit()

	player.update(deltatime)


class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.velx = 0
		self.vely = 0
		self.sprite = loadasset('tempcharacter')

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

	def render(self):
		display.blit(self.sprite, (self.x, self.y))


pygame.init()
pygame.display.set_caption('Flash Card Thing')
running = True
FPS = 60
WIDTH = 1280	 
HEIGHT = 720 
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME, 32)
display = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BGCOLOR = (19, 27, 35)
GAMEPATH = sys.path[0]
player = Player(100, 100)


def main():
	while running:
		deltatime = clock.tick(FPS)
		tick(deltatime)
		render()
		screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
		pygame.display.update()


if __name__ == '__main__':
	main()

