# Utilities #

import sys 

def loadasset(name, pg):
	asset = pg.image.load(f'{sys.path[0]}/Assets/{name}.png').convert()
	asset.set_colorkey((0, 0, 0))
	return asset;

