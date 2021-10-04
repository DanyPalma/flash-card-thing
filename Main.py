#!/usr/bin/env python

import os
import sys
import time
import pygame
from pygame.locals import *


pygame.init()
pygame.display.set_caption('29 Days Out')
running = True
FPS = 60
WIDTH = 680	 
HEIGHT = 480 
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME , 32)
display = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BGCOLOR = (19, 27, 35)


def render():
	display.fill(BGCOLOR)


def events():
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
			pygame.quit()
			sys.exit()


def main():
	while running:
		render()
		events()
		screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
		pygame.display.update()
		clock.tick(FPS)


if __name__ == '__main__':
	main()

