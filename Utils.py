# Utilities #

import sys 

ASSETS = []

def loadasset(name, pg):
	asset = pg.image.load(f'{sys.path[0]}/Static/{name}.png').convert()
	asset.set_colorkey((0, 0, 0))
	return asset;

def initassets(pg):
	global ASSETS
	ASSETS.append(loadasset('prompt', pg))
	ASSETS.append(loadasset('menubg', pg))

