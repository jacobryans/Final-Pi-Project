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
pygame.key.set_repeat(1, 20) 
door = pygame.image.load('door.png')
screen.blit(door, (250, 0))
screen.blit(pic1, (0, 0))
screen.blit(d, (250, 250))
pygame.display.init()
pygame.display.update()

def movedetection():
    x_speed = 4
    y_speed = 4
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                x_speed = 8
                y_speed = 8
            elif event.key == pygame.K_LEFT:
                pic = l
                if player.px > 0 and player.px < 500:
                    player.move(-x_speed, 0)
                    player.px -= x_speed
                else:
                    player.px = 50
                screen.blit(pic1, (0,0))
                screen.blit(pic, (player.px, player.py))
            elif event.key == pygame.K_RIGHT:
                pic = r
                if player.px > 0 and player.px < 500:
                    player.move(x_speed,0)
                    player.px += x_speed
                else:
                    player.px = 450
                screen.blit(pic1, (0, 0))
                screen.blit(pic, (player.px, player.py))
            elif event.key == pygame.K_UP:
                pic = u
                if player.py > 0 and player.py < 500:
                    player.py -= y_speed
                    player.move(0, y_speed)
                else:
                    player.py = 50
                screen.blit(pic1, (0, 0))
                screen.blit(pic, (player.px, player.py))
            elif event.key == pygame.K_DOWN:
                pic = d
                if player.py > 0 and player.py < 500:
                    player.py += y_speed
                    player.move(0, -y_speed)
                else:
                    player.py = 450
                screen.blit(pic1, (0, 0))
                screen.blit(pic, (player.px, player.py))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                x_speed = 4
                y_speed = 4
    
        
class Player(pygame.sprite.Sprite):
    
    def __init__(self, (px, py), room):
        self.room = room
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
        self.player.center[0] += x
        self.player.center[1] += y
##        if self.rect.x > 0 and self.rect.x < 500:
##            self.move_single_axis(x_speed, 0)
##        if self.rect.y > 0 and self.rect.y < 500:
##            self.move_single_axis(0, y_speed)
    
    def update(self):
        # Move the player
        self.speedx = 0
        self.speedy = 0
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
        self.rect.x += self.speedx
        if self.rect.right > 500:
                self.rect.right = 500
        if self.rect.left < 0:
                self.rect.left = 0
        if self.rect.bottom > 500:
                self.rect.bottom = 500
        if self.rect.top < 0:
                self.rect.top = 0
##        self.rect.x += x_speed
##        self.rect.y += y_speed

        # If you collide with a exit, move to the next room
    def exitdetection(self, exits):
        for exit in exits:
            if self.rect.colliderect(exit_rect):
                if self.px > 490  and directions[3] in self.room.exits: # East Exit
                    newexit = 'west'
                    load = True
                    roomchange(self.room.exits.index(exit))
                    self.room = currentRoom
                    if newexit in currentRoom.exits is False:
                        currentRoom.addExit(newexit)
                elif self.px < 10 and directions[2] in self.room.exits: # West Exit
                    newexit = 'east'
                    load = True
                    roomchange(self.room.exits.index(exit))
                    self.room = currentRoom
                    if newexit in currentRoom.exits is False:
                        currentRoom.addExit(newexit)
                elif self.py > 490 and directions[1] in self.room.exits: # South Exit
                    newexit = 'north'
                    load = True
                    roomchange(self.room.exits.index(exit))
                    self.room = currentRoom
                    if newexit in currentRoom.exits is False:
                        currentRoom.addExit(newexit)
                elif self.py < 10 and directions[0] in self.room.exits: # South Exit
                    newexit = 'south'
                    load = True
                    roomchange(self.room.exits.index(exit))
                    self.room = currentRoom
                    if newexit in currentRoom.exits is False:
                        currentRoom.addExit(newexit)

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
    def __init__(self, xcord, ycord):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image = door
        self.rect = self.image.get_rect()
        self.rect.centerx = xcord
        self.rect.centery = ycord

    def collide(self, x, y):
        if self.rect.collidepoint(x, y):
            print 'hit'

    def setupsprites():
        exit0_rect = Exits(roomvars[str(currentRoom.name)]['exitlocs'][0])
        exit1_rect = Exits(roomvars[str(currentRoom.name)]['exitlocs'][1])
        exit2_rect = Exits(roomvars[str(currentRoom.name)]['exitlocs'][2])
        exit3_rect = Exits(roomvars[str(currentRoom.name)]['exitlocs'][3])
        
        

    def colliding():
        exit0_rect.collide(player.rect.centerx, player.rect.centery)
        exit1_rect.collide(player.rect.centerx, player.rect.centery)
        exit2_rect.collide(player.rect.centerx, player.rect.centery)
        exit3_rect.collide(player.rect.centerx, player.rect.centery)


a1 = Area('testarea')
global currentRoom
currentRoom = a1.rooms[0]
player = Player((5,5),a1.rooms[0])

while True:
    colliding()
    player.exitdetection(player.room.exits)
    if e0 == True:
        pygame.draw.rect(screen, (200, 200, 200), exit0_rect)
    if e1 == True:
        pygame.draw.rect(screen, (200, 200, 200), exit1_rect)
    if e2 == True:
        pygame.draw.rect(screen, (200, 200, 200), exit2_rect)
    if e3 == True:
        pygame.draw.rect(screen, (200, 200, 200), exit3_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.display.update()
    root.update()

