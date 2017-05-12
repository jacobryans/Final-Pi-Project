import os
import sys
import time
from pygame import *
import Tkinter as tk
from Tkinter import *
from Objects import *
from Defs import MapDefs

directions = [ 'north','south','west','east']

root = tk.Tk()
embed = tk.Frame(root, width = 500, height = 500) #creates embed frame for pygame window
embed.grid(columnspan = (500), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
buttonwin = tk.Frame(root, width = 0, height = 500)
buttonwin.pack(side = LEFT)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color(60,60,100))
global d, l, r, u, door, doorp, loadscreen
loadscreen = pygame.image.load('Loadscreen.png')
d = pygame.image.load('1.png')
l = pygame.image.load('2.png')
r = pygame.image.load('3.png')
u = pygame.image.load('4.png')
pygame.key.set_repeat(1, 10)
door = pygame.image.load('door.png')
doorp = pygame.image.load('doorp.png')
gamecomplete = False
loading = None
interact = False
#screen.blit(d, (250, 250))
pygame.display.init()
pygame.display.update()

class Player(object):
    def __init__(self, room, first):
        self.room = room
        self.first = first

    def first(self, value=None):
        if (value == None):
            return self._first
        self._first = value

    def area(self, value=None):
        if (value == None):
            return self._area
        self._area = value
    
    def room(self, value=None):
        if (value == None):
            return self._room
        self._room = value

class PlayerSprite(pygame.sprite.Sprite):
    
    def __init__(self, px ,py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((px, py))
        self.image = pygame.image.load('1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = px
        self.rect.centery = py

    def px(self, value=None):
        if (value == None):
            return self._px
        self._px = value

    def py(self, value=None):
        if (value == None):
            return self._py
        self._py = value

    def move(self, x, y):
        self.player.center[0]
        self.player.center[1]

    def update(self):
        self.speedx = 5
        self.speedy = 5
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
                self.image = pygame.image.load('2.png')
                self.rect.centerx -= 5
        if keystate[pygame.K_RIGHT]:
                self.image = pygame.image.load('3.png')
                self.rect.centerx += 5
        if keystate[pygame.K_UP]:
                self.image = pygame.image.load('4.png')
                self.rect.centery -= 5
        if keystate[pygame.K_DOWN]:
                self.image = pygame.image.load('1.png')
                self.rect.centery += 5
        if keystate[pygame.K_e]:
                global interact
                interact = True
        if keystate[pygame.K_a]:
                print(player.room)
        if keystate[pygame.K_s]:
                print(player.room.locations[0], player.room.locations[1])
        if keystate[pygame.K_d]:
                print()
        if keystate[pygame.K_f]:
                print(psprite.rect.centerx)
        if keystate[pygame.K_g]:
                print(psprite.rect.centery)
        if self.rect.right > 500:
                self.rect.right = 500
        if self.rect.left < 0:
                self.rect.left = 0
        if self.rect.bottom > 500:
                self.rect.bottom = 500
        if self.rect.top < 0:
                self.rect.top = 0

    def roomchange(self, index, px, py):
            loading = True
            while loading == True:
                player.room = player.room.locations[index]
                screen.blit(loadscreen, (0, 0))
                #exitcheck()
                pygame.display.update()
                pygame.time.delay(2000)
                #bgupdate('background')
                psprite.rect.centerx = px
                psprite.rect.centery = py
                player_sprites.draw(screen)
                reset()
                pygame.display.update() 
                loading = False

    def areachange(self, room):
        loading = True
        while loading == True:
            if player.room.name == 'area1exit':
                player.area = area2
                player.room = area2.rooms[0]
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                pygame.time.delay(4000)
                player_sprites.draw(screen)
                reset()
                pygame.display.update()
                loading = False
            elif player.room.name == 'area2exit':
                player.area = area3
                player.room = area3.rooms[0]
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                pygame.time.delay(4000)
                player_sprites.draw(screen)
                reset()
                pygame.display.update()
                loading = False
            elif player.room.name == 'area3exit':
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                pygame.time.delay(4000)
                player_sprites.draw(screen)
                reset()
                pygame.display.update()
                loading = False

class Items(pygame.sprite.Sprite):
    
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.Surface((50,40))
        self.image = pygame.image.load(items[self.name]['pic'])
        self.rect = self.image.get_rect()
        (self.rect.centerx, self.rect.centery) = roomvars[player.room.name]['itempos'][randint(0, 1)]
        self.location = areas[player.area.name]['itemloc'][0]
        self.type = items[self.name]['type']                        
        self.key = items[self.name]['key']
        self.desc = items[self.name]['desc']

    def name(self, value=None):
        if value==None:
            return self._name
        self._name = value

    def collide(self, rect):
        if self.rect.colliderect(rect):
            if self.type == 'readable':
                while interact == True:
                    screen.blit(self.image, (250, 250))
                    screen.fill(255,255,255)
            if self.type == 'usable':
                a1puzzle = raw_input('Hack Out - What is the answer to the first terminal puzzle?')
                a2puzzle = raw_input('Hack Out - What is the answer to the first terminal puzzle?')
                a3puzzle = raw_input('Hack Out - What is the answer to the first terminal puzzle?')
                if a1puzzle == '#':
                    area1.complete = True
                if a2puzzle == '#':
                    area2.complete = True
                if a3puzzle == '#':
                    area3.complete = True
            
            
    def itemsetup(self):
        # checks to see if item locations are in the same area as player and adds them to sprites
        if items['terminal'] in areas[player.area]['itemlist'] and self.location == player.area.rooms.index(player.room):
            item_sprites.add(terminal)
        if items['key1'] in areas[player.area]['itemlist'] and self.location == player.area.rooms.index(player.room):
            item_sprites.add(key1)
        if items['key2'] in areas[player.area]['itemlist'] and self.location == player.area.rooms.index(player.room):
            item_sprites.add(key2)
        if items['key3'] in areas[player.area]['itemlist'] and self.location == player.area.rooms.index(player.room):
            item_sprites.add(key3)

class Exits(pygame.sprite.Sprite):
    
    def __init__(self, (xcord, ycord), areaportal = False):
        # exit init
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.areaportal = areaportal
        self.image = self.imagechanger(self.areaportal)
        self.rect = self.image.get_rect()
        self.rect.centerx = xcord
        self.rect.centery = ycord

    def areaportal(self, value=None):
        if value==None:
            return self._areaportal
        self._areaportal = value

    def imagechanger(self, areaportal):
        if areaportal == True:
            self.image = doorp
        for i in roomvars[player.room.name]['exitindex']:
            if i == 6:
                areaportal = True
                self.image = doorp
            else:
                self.image = door
            return self.image


    def collide(self, rect):
        if self.rect.colliderect(rect):
            if 6 in roomvars[player.room.name]['exitindex'] and exit1.rect.colliderect(rect):
                psprite.areachange(player.room.name)
            if exit3.rect.colliderect(rect) and 'east' in roomvars[player.room.name]['exits']: # East Exit
                print "east"
                psprite.roomchange(player.room.exits.index('east'), 50 ,220)
            elif exit2.rect.colliderect(rect) and 'west' in roomvars[player.room.name]['exits']: # West Exit
                print "west"
                psprite.roomchange(player.room.exits.index('west'), 440, 220)
            elif exit1.rect.colliderect(rect) and 'south' in roomvars[player.room.name]['exits']: # South Exit
                print "south"
                psprite.roomchange(player.room.exits.index('south'), 220, 50)
            elif exit0.rect.colliderect(rect) and 'north' in roomvars[player.room.name]['exits']: # North Exit
                print "north"
                psprite.roomchange(player.room.exits.index('north'), 220, 440)
            

    def exitsetup(self):
        if 'north' in roomvars[player.room.name]['exits']:
            exit_sprites.add(exit0)
        if 'south' in roomvars[player.room.name]['exits']:
            exit_sprites.add(exit1)
        if 'west' in roomvars[player.room.name]['exits']:
            exit_sprites.add(exit2)
        if 'east' in roomvars[player.room.name]['exits']:
            exit_sprites.add(exit3)


def bgupdate(name):
    if name == 'loadscreen':
        background = pygame.image.load('Loadscreen.png')
        return background
    elif name == 'background':
        background = pygame.image.load(roomvars[player.room.name]['background'][0])
        return background


def start():
    global exit0, exit1, exit2, exit3, background, exit_sprites, player_sprites, ind
    exit0 = Exits(roomvars[player.room.name]['exitlocs'][0])
    exit1 = Exits(roomvars[player.room.name]['exitlocs'][1])
    exit2 = Exits(roomvars[player.room.name]['exitlocs'][2])
    exit3 = Exits(roomvars[player.room.name]['exitlocs'][3])
    terminal = Items('terminal')
    key1 = Items('key1')
    key2 = Items('key2')
    key3 = Items('key3')
    exitlist = [ exit0, exit1, exit2, exit3 ]
    for i in range(len(exitlist)):
        exitlist[i].imagechanger(areaportal = False)
    player_sprites = pygame.sprite.Group()
    exit_sprites = pygame.sprite.Group()
    item_sprites = pygame.sprite.Group()
    player.first = False
    background = bgupdate('background')

global reset

def reset():
    background, player_sprites, exit_sprites, player.first = None, None, None, False
    start()


def colliding():
    exit0.collide(psprite.rect)
    exit1.collide(psprite.rect)
    exit2.collide(psprite.rect)
    exit3.collide(psprite.rect)

def exitcheck():
    exit0.exitsetup()
    exit1.exitsetup()
    exit2.exitsetup()
    exit3.exitsetup()

player = Player(area1.rooms[0], True)
player.area = area1
start()
global psprite
psprite = PlayerSprite(250, 250)
clock = pygame.time.Clock()
while gamecomplete == False:
    clock.tick(60)
    player_sprites.add(psprite)
    screen.blit(background,(0,0))
    exitcheck()
    colliding()
    psprite.update()
    player_sprites.draw(screen)
    exit_sprites.draw(screen)
    if area1.complete == True and area2.complete == True and area3.complete == True:
        gamecomplete = True
    pygame.display.update()
    root.update()

