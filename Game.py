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
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
buttonwin = tk.Frame(root, width = 75, height = 500)
buttonwin.pack(side = LEFT)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color(60,60,100))
global d, l, r, u, door, loadscreen
loadscreen = pygame.image.load('Loadscreen.png')
d = pygame.image.load('1.png')
l = pygame.image.load('2.png')
r = pygame.image.load('3.png')
u = pygame.image.load('4.png')
pygame.key.set_repeat(1, 10) 
door = pygame.image.load('door.png')
loading = None
#screen.blit(d, (250, 250))
pygame.display.init()
pygame.display.update()

class Player(object):
    def __init__(self, room, first = True):
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
        self.speedx = 1
        self.speedy = 1
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
                self.image = pygame.image.load('2.png')
                self.rect.centerx -= 1
        if keystate[pygame.K_RIGHT]:
                self.image = pygame.image.load('3.png')
                self.rect.centerx += 1
        if keystate[pygame.K_UP]:
                self.image = pygame.image.load('4.png')
                self.rect.centery -= 1
        if keystate[pygame.K_DOWN]:
                self.image = pygame.image.load('1.png')
                self.rect.centery += 1
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
            pygame.time.delay(1500)
            #bgupdate('background')
            psprite = None
            psprite = PlayerSprite(px, py)
            player_sprites.add(psprite)
            reset()
            pygame.display.update()
            loading = False
        

class Exits(pygame.sprite.Sprite):
    
    def __init__(self, (xcord, ycord), active = False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image = door
        self.rect = self.image.get_rect()
        self.rect.centerx = xcord
        self.rect.centery = ycord
        self.active = active
        
    def active(self, value=None):
        if value==None:
            return self._active
        self._active = value


    def collide(self, active):
        if self.rect.colliderect(psprite.rect):
           # while self.active == True:
            if psprite.rect.colliderect(exit3) and 'east' in roomvars[player.room.name]['exits']: # East Exit
                print "east"
                psprite.roomchange(player.room.exits.index('east'), 50 ,220)
                self.active = False
            elif 'east' in roomvars[player.room.name]['exits'] is False:
                print "This is not a viable exit!"
            elif psprite.rect.colliderect(exit2) and 'west' in roomvars[player.room.name]['exits']: # West Exit
                print "west"
                psprite.roomchange(player.room.exits.index('west'), 440, 220)
                self.active = False
            elif 'west' in roomvars[player.room.name]['exits'] is False:
                print "This is not a viable exit!"
            elif psprite.rect.colliderect(exit1) and 'south' in roomvars[player.room.name]['exits']: # South Exit
                print "south"
                psprite.roomchange(player.room.exits.index('south'), 220, 50)
                self.active = False
            elif 'south' in roomvars[player.room.name]['exits'] is False:
                print "This is not a viable exit!"
            elif psprite.rect.colliderect(exit0) and 'north' in roomvars[player.room.name]['exits']: # North Exit
                print "north"
                psprite.roomchange(player.room.exits.index('north'), 220, 440)
                self.active = False
            elif 'north' in roomvars[player.room.name]['exits'] is False:
                print "This is not a viable exit!"
            

    def exitsetup(self):
        if 'north' in roomvars[player.room.name]['exits']:
            exit_sprites.add(exit0)
            self.active = True
        if 'south' in roomvars[player.room.name]['exits']:
            exit_sprites.add(exit1)
            self.active = True
        if 'west' in roomvars[player.room.name]['exits']:
            exit_sprites.add(exit2)
            self.active = True
        if 'east' in roomvars[player.room.name]['exits']:
            exit_sprites.add(exit3)
            self.active = True


def bgupdate(name):
    if name == 'loadscreen':
        background = pygame.image.load('Loadscreen.png')
        return background
    elif name == 'background':
        background = pygame.image.load(roomvars[player.room.name]['background'][0])
        return background


def start():
    global player, psprite, exit0, exit1, exit2, exit3, background, exit_sprites, player_sprites
    exit0 = Exits(roomvars[str(player.room.name)]['exitlocs'][0])
    exit1 = Exits(roomvars[str(player.room.name)]['exitlocs'][1])
    exit2 = Exits(roomvars[str(player.room.name)]['exitlocs'][2])
    exit3 = Exits(roomvars[str(player.room.name)]['exitlocs'][3])
    player_sprites = pygame.sprite.Group()
    exit_sprites = pygame.sprite.Group()
    if player.first == True:
        psprite = PlayerSprite(200, 200)
    player.first = False
    player_sprites.add(psprite)
    background = bgupdate('background')

global reset

def reset():
    background, exit_sprites, player.first = None, None, False
    start()


def colliding():
    exit0.collide(exit0.active)
    exit1.collide(exit1.active)
    exit2.collide(exit2.active)
    exit3.collide(exit3.active)

def exitcheck():
    exit0.exitsetup()
    exit1.exitsetup()
    exit2.exitsetup()
    exit3.exitsetup()

player = Player(testarea.rooms[0])
clock = pygame.time.Clock()
while True:
    clock.tick(120)
    if player.first == True:
        start()
    screen.blit(background,(0,0))
    exitcheck()
    colliding()
    psprite.update()
    player_sprites.draw(screen)
    exit_sprites.draw(screen)
    pygame.display.update()
    root.update()

