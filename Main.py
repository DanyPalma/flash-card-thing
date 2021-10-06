#!/usr/bin/env python

import os
import sys
import time
import pygame
from pygame.locals import *
import Utils as u
import Player as Player
import Entity as Entity


def render():
	display.fill(BGCOLOR)
#	for e in entities:
#		e.render(display)
	player.render(display)


def tick(deltatime):
	pressed = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
			pygame.quit()
			sys.exit()

	player.update(deltatime, pressed)


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
entities = []
player = Player.Player(100, 100, pygame)
table = Entity.Entity('tf', 1000, 400, pygame)
entities.append(table)


def main():
	while running:
		deltatime = clock.tick(FPS)
		tick(deltatime)
		render()
		screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
		pygame.display.update()


if __name__ == '__main__':
	main()

