import os
import sys
import pygame
import Tkinter as tk
from Tkinter import *
from Objects import *
from Defs import MapDefs

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
pic1 = pygame.image.load('Background.gif')
global d, l, r, u, door
d = pygame.image.load('1.png')
l = pygame.image.load('2.png')
r = pygame.image.load('3.png')
u = pygame.image.load('4.png')
e0 = False
e1 = False
e2 = False
e3 = False
pygame.key.set_repeat(1, 20) 
door = pygame.image.load('door.png')
screen.blit(door, (250, 0))
screen.blit(pic1, (0, 0))
#screen.blit(d, (250, 250))
pygame.display.init()
pygame.display.update()

class Player(object):
    def __init__(self, room):
        self.room = room

##    def collide(self, x = psprite.px, y = psprite.py, exits=None):
##        if self.rect.collidepoint(x, y):
##            for exit in exits:
##                if psprite.px   and directions[3] in self.room.exits: # East Exit
##                    newexit = 'west'
##                    load = True
##                    roomchange(self.room.exits.index(exit))
##                    self.room = currentRoom
##                    if newexit in currentRoom.exits is False:
##                        currentRoom.addExit(newexit)
##                elif psprite.px < 10 and directions[2] in self.room.exits: # West Exit
##                    newexit = 'east'
##                    load = True
##                    roomchange(self.room.exits.index(exit))
##                    self.room = currentRoom
##                    if newexit in currentRoom.exits is False:
##                        currentRoom.addExit(newexit)
##                elif psprite.py > 490 and directions[1] in self.room.exits: # South Exit
##                    newexit = 'north'
##                    load = True
##                    roomchange(self.room.exits.index(exit))
##                    self.room = currentRoom
##                    if newexit in currentRoom.exits is False:
##                        currentRoom.addExit(newexit)
##                elif psprite.py < 10 and directions[0] in self.room.exits: # South Exit
##                    newexit = 'south'
##                    load = True
##                    roomchange(self.room.exits.index(exit))
##                    self.room = currentRoom
##                    if newexit in currentRoom.exits is False:
##                        currentRoom.addExit(newexit)

class PlayerSprite(pygame.sprite.Sprite):
    
    def __init__(self, px ,py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
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
        # Move each axis separately. Note that this checks for collisions both times.
        self.player.center[0]
        self.player.center[1]

    def update(self):
        self.speedx = 1
        self.speedy = 1
        if self.rect.collidepoint(500, 500):
            colliding()
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
        if self.rect.right > 500:
                self.rect.right = 500
        if self.rect.left < 0:
                self.rect.left = 0
        if self.rect.bottom > 500:
                self.rect.bottom = 500
        if self.rect.top < 0:
                self.rect.top = 0

    def roomchange(self, index):
        while load == True:
            currentRoom = p.room.locations[index]
            if directions[0] in currentRoom.exits:
                # can add more load features here
                # this just blits exits around the room based on roomtype and the coords from the dictionary
                screen.blit(door, roomvars[str(currentRoom.name)]['exitlocs'][0])
                e0 = True
            if directions[1] in currentRoom.exits:
                screen.blit(door, roomvars[str(currentRoom.name)]['exitlocs'][1])
                e1 = True
            if directions[2] in currentRoom.exits:
                screen.blit(door, roomvars[str(currentRoom.name)]['exitlocs'][2])
                e2 = True
            if directions[3] in currentRoom.exits:
                screen.blit(door, roomvars[str(currentRoom.name)]['exitlocs'][3])
                e3 = True
            load = False
            #e0, e1, e2, e3 = False

class Exits(pygame.sprite.Sprite):
    def __init__(self, (xcord, ycord)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image = door
        self.rect = self.image.get_rect()
        self.rect.centerx = xcord
        self.rect.centery = ycord

    def collide(self, x, y, exits=None):
        if self.rect.collidepoint(x, y):
            for exit in exits:
                if x > 490 and directions[3] in player.room.exits: # East Exit
                    newexit = 'west'
                    load = True
                    player.room = currentRoom
                    roomchange(self.room.exits.index(exit))
                    if newexit in currentRoom.exits is False:
                        currentRoom.addExit(newexit)
                elif x < 10 and directions[2] in player.room.exits: # West Exit
                    newexit = 'east'
                    load = True
                    player.room = currentRoom
                    roomchange(self.room.exits.index(exit))
                    if newexit in currentRoom.exits is False:
                        currentRoom.addExit(newexit)
                elif y > 490 and directions[1] in player.room.exits: # South Exit
                    newexit = 'north'
                    load = True
                    player.room = currentRoom
                    roomchange(self.room.exits.index(exit))
                    if newexit in currentRoom.exits is False:
                        currentRoom.addExit(newexit)
                elif y < 10 and directions[0] in player.room.exits: # South Exit
                    newexit = 'south'
                    load = True
                    player.room = currentRoom
                    roomchange(self.room.exits.index(exit))
                    if newexit in currentRoom.exits is False:
                        currentRoom.addExit(newexit)
                else:
                    break

def setupsprites():
    exit0 = Exits(roomvars[str(currentRoom.name)]['exitlocs'][0])
    exit1 = Exits(roomvars[str(currentRoom.name)]['exitlocs'][1])
    exit2 = Exits(roomvars[str(currentRoom.name)]['exitlocs'][2])
    exit3 = Exits(roomvars[str(currentRoom.name)]['exitlocs'][3])
    
def colliding():
    exit0.collide(psprite.rect.centerx, psprite.rect.centery)
    exit1.collide(psprite.rect.centerx, psprite.rect.centery)
    exit2.collide(psprite.rect.centerx, psprite.rect.centery)
    exit3.collide(psprite.rect.centerx, psprite.rect.centery)

def spriteadd():
    if (e0 is True) and (directions[0] in all_sprites.sprites()) == False:
        all_sprites.add(exit0)
    elif (e1 is True) and (directions[1] in all_sprites.sprites()) == False:
        all_sprites.add(exit1)
    elif (e2 is True) and (directions[2] in all_sprites.sprites()) == False:
        all_sprites.add(exit2)
    elif (e3 is True) and (directions[3] in all_sprites.sprites()) == False:
        all_sprites.add(exit3)
    else:
        pass

def spriterm():
    if (e0 is False) and (directions[0] in all_sprites.sprites()):
        all_sprites.remove(exit0)
    elif (e1 is False) and (directions[1] in all_sprites.sprites()):
        all_sprites.remove(exit1)
    elif (e2 is False) and (directions[2] in all_sprites.sprites()):
        all_sprites.remove(exit2)
    elif (e3 is False) and (directions[3] in all_sprites.sprites()):
        all_sprites.remove(exit3)
    else:
        pass

a1 = Area('testarea')
global currentRoom
currentRoom = a1.rooms[0]
player = Player(a1.rooms[0])
psprite = PlayerSprite(50, 50)
all_sprites = pygame.sprite.Group()
all_sprites.add(psprite)

while True:
    screen.blit(pic1, (0,0))
    psprite.update()
    setupsprites()
    spriteadd()
    all_sprites.update()
    spriterm()
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
    root.update()

