import os
import sys
import time
from pygame import *
import Tkinter as tk
from Tkinter import *
from Objects import *
from Defs import MapDefs

directions = [ 'north','south','west','east']
pygame.mixer.init()
sound = pygame.mixer.Sound('music1.mp3')
root = tk.Tk()
embed = tk.Frame(root, width = 500, height = 500) #creates embed frame for pygame window
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
buttonwin = tk.Frame(root, width = 75, height = 500)
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
doorp = pygame.image.load('doorp.gif')
loading = None
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
                pass
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
                player.room = area2.rooms[0]
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                pygame.time.delay(4000)
                player_sprites.draw(screen)
                reset()
                pygame.display.update()
                loading = False
            elif player.room.name == 'area2exit':
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

##class Puzzle(pygame.sprite.Sprite);

class Exits(pygame.sprite.Sprite):
    
    def __init__(self, (xcord, ycord), ind6 = False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.ind6 = ind6
        self.image = self.imagechanger(self.ind6)
        self.rect = self.image.get_rect()
        self.rect.centerx = xcord
        self.rect.centery = ycord

    def ind6(self, value=None):
        if value==None:
            return self._ind6
        self._ind6 = value

    def imagechanger(self, ind6):
        if ind6 == True:
            self.image = doorp
        for i in roomvars[player.room.name]['exitindex']:
            if i == 6:
                ind6 = True
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
    exitlist = [ exit0, exit1, exit2, exit3 ]
    for i in range(len(exitlist)):
        exitlist[i].imagechanger(ind6 = True)
    player_sprites = pygame.sprite.Group()
    exit_sprites = pygame.sprite.Group()
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
start()
global psprite
psprite = PlayerSprite(250, 250)
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    player_sprites.add(psprite)
    screen.blit(background,(0,0))
    exitcheck()
    colliding()
    psprite.update()
    player_sprites.draw(screen)
    exit_sprites.draw(screen)
    pygame.display.update()
    root.update()

