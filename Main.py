#!/usr/bin/env python

import os
import sys
import time
import pygame
from pygame.locals import *
import Utils as u
import Player as Player
import Entity as Entity
import random
from pygame import mixer

#states#
import Room as room 
import Flashcard as flashcard
import CreateFlashcardSet as createset

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Flash Card Thing')
running = True
FPS = 60 
WIDTH = 1280	 
HEIGHT = 720 
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME, 0)
display = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BGCOLOR = (19, 27, 35)
GAMEPATH = sys.path[0]
state = [None, room, flashcard, createset]
CURRENTSTATE = 1 

 # this is if we want to choose like a random mp3 or something 
 #path = './Music/'
 #all_mp3 = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp3')]

 #randomFile = random.choice(all_mp3) 

backgroundMusic = ("./Music/8bit/Zelda.mp3")

pygame.mixer.music.load(backgroundMusic)
pygame.mixer.music.play(-1)

def main():
	global CURRENTSTATE
	state[1].init(pygame, Player, Entity)
	while running:
		TEMP = CURRENTSTATE
		deltatime = clock.tick(FPS)
		screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
		CURRENTSTATE = state[CURRENTSTATE].update(pygame, display, deltatime, TEMP)
		pygame.display.update()
		if CURRENTSTATE != TEMP:
			state[CURRENTSTATE].init(pygame, Player, Entity)

if __name__ == '__main__':
	u.initassets(pygame)
	main()
	pygame.mixer.Music.set_volume(backgroundMusic, 0.5)
