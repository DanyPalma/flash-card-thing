#!/usr/bin/env python

import os
import sys
import time
import pygame
from pygame.locals import *

import Player as Player

def render():
	display.fill(BGCOLOR)
	player.render(display)

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
player = Player.Player(100, 100, pygame)


def main():
	while running:
		deltatime = clock.tick(FPS)
		tick(deltatime)
		render()
		screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
		pygame.display.update()


if __name__ == '__main__':
	main()

