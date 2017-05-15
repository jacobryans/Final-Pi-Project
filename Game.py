import os
import sys
import time
import inputbox
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
d = ['pic/down1.png','pic/down2.png','pic/down3.png', 'pic/down4.png']
l = ['pic/left1.png','pic/left2.png','pic/left3.png', 'pic/left4.png']
r = ['pic/right1.png','pic/right2.png','pic/right3.png', 'pic/right4.png']
u = ['pic/up1.png','pic/up2.png','pic/up3.png', 'pic/up4.png']
door = pygame.image.load('pic/door.png')
doorp = pygame.image.load('pic/doorp.png')
gamecomplete = False
loading = None
interact = False
#screen.blit(d, (250, 250))
pygame.display.set_caption('Hack.Out v1')
pygame.display.init()
pygame.display.update()

class Player(object):
    def __init__(self, room):
        self.room = room

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
        self.image = pygame.image.load('pic/up1.png')
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
        self.speedx = 3
        self.speedy = 3
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
                clock.tick(60)
                self.image = pygame.image.load(l[0])
                self.rect.centerx -= 3
                player_sprites.add(self)
                player_sprites.draw(screen)
                self.image = pygame.image.load(l[1])
                self.rect.centerx -= 3
                player_sprites.add(self)
                player_sprites.draw(screen)
                self.image = pygame.image.load(l[2])
                self.rect.centerx -= 3
                player_sprites.add(self)
                player_sprites.draw(screen)
                self.image = pygame.image.load(l[3])
                self.rect.centerx -=  2
                player_sprites.draw(screen)
        if keystate[pygame.K_RIGHT]:
                clock.tick(60)
                self.image = pygame.image.load(r[0])
                self.rect.centerx += 3
                pygame.time.delay(5)
                self.image = pygame.image.load(r[1])
                self.rect.centerx += 3
                pygame.time.delay(5)
                self.image = pygame.image.load(r[2])
                self.rect.centerx += 3
                pygame.time.delay(5)
                self.image = pygame.image.load(r[3])
                self.rect.centerx += 3
                pygame.time.delay(5)
        if keystate[pygame.K_UP]:
                clock.tick(60)
                self.image = pygame.image.load(u[0])
                self.rect.centery -= 3
                pygame.time.delay(5)
                self.image = pygame.image.load(u[1])
                self.rect.centery -= 3
                pygame.time.delay(5)
                self.image = pygame.image.load(u[2])
                self.rect.centery -= 3
                pygame.time.delay(5)
                self.image = pygame.image.load(u[3])
                self.rect.centery -= 3
                pygame.time.delay(5)
        if keystate[pygame.K_DOWN]:
                clock.tick(60)
                self.image = pygame.image.load(d[0])
                self.rect.centery += 3
                pygame.time.delay(5)
                self.image = pygame.image.load(d[1])
                self.rect.centery += 3
                pygame.time.delay(5)
                self.image = pygame.image.load(d[2])
                self.rect.centery += 3
                pygame.time.delay(5)
                self.image = pygame.image.load(d[3])
                self.rect.centery += 3
                pygame.time.delay(5)
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
                pygame.display.update()
                pygame.time.delay(2000)
                self.rect.centerx = px
                self.rect.centery = py
                pygame.display.update()
                pygame.time.delay(3000)
                reset()
                pygame.display.update() 
                loading = False

    def areachange(self, room):
        loading = True
        while loading == True:
            if player.room.name == 'area1exit' and area1.complete == True:
                player.area = area2
                player.room = area2.rooms[0]
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                pygame.time.delay(4000)
                player_sprites.draw(screen)
                reset()
                pygame.display.update()
                loading = False
            elif player.room.name == 'area2exit' and area2.complete == True:
                player.area = area3
                player.room = area3.rooms[0]
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                pygame.time.delay(4000)
                player_sprites.draw(screen)
                reset()
                pygame.display.update()
                loading = False
            elif player.room.name == 'area3exit' and area3.complete == True:
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                pygame.time.delay(4000)
                player_sprites.draw(screen)
                reset()
                pygame.display.update()
                loading = False
            else:
                reset()
                loading = False

class AnySprite(pygame.sprite.Sprite):
    def __init__(self, imagename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((500,500))
        self.image = pygame.image.load(imagename)
        self.rect = self.image.get_rect()

class Items(pygame.sprite.Sprite):
    def __init__(self, name, px, py):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.Surface((500, 500))
        self.image = pygame.image.load(items[self.name]['pic'][0])
        self.rect = self.image.get_rect()
        self.rect.centerx = px
        self.rect.centery = py
        self.type = items[self.name]['type']                        
        self.key = items[self.name]['key']
        self.desc = items[self.name]['desc']

    def collide(self, rect):
        if self.rect.colliderect(psprite.rect):
            if self == terminal:
                termcollide = True
                while termcollide == True:
                    if player.room.name == 'area1r1':
                        puzzleterminal = AnySprite('pic/puzzleterminal1.png')
                        any_sprites = pygame.sprite.Group()
                        any_sprites.add(puzzleterminal)
                        any_sprites.draw(screen)
                        pygame.display.update()
                    elif player.room.name == 'area2r3':
                        puzzleterminal = AnySprite('pic/puzzleterminal2.png')
                        any_sprites = pygame.sprite.Group()
                        any_sprites.add(puzzleterminal)
                        any_sprites.draw(screen)
                        pygame.display.update()
                    elif player.room.name == 'area3r2':
                        puzzleterminal = AnySprite('pic/puzzleterminal3.png')
                        any_sprites = pygame.sprite.Group()
                        any_sprites.add(puzzleterminal)
                        any_sprites.draw(screen)
                        pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LSHIFT:
                                reset()
                                termcollide = False
                                break
            elif self.key == True:
                if self.name == 'key1':
                    screen.fill((0,0,0))
                    answer = inputbox.ask(screen, 'Answer: ')
                    if answer == 'theanswertoallanswers':
                        reset()
                        area1.complete = True
                elif self.name == 'key2':
                    answer = inputbox.ask(screen, "Area 1 Puzzle Answer: ")
                    if a2puzzle == '15':
                        area2.complete = True
                elif self.name == 'key3':
                    answer = inputbox.ask(screen, "Area 1 Puzzle Answer: ")
                    if a3puzzle == '20':
                        area3.complete = True
            
    def itemsetup(self):
        # checks to see if item locations are in the same area as player and adds them to sprites:
        if items['terminal'] in roomvars[player.room.name]['itemlist']:
            item_sprites.add(terminal)
        elif items['key1'] in roomvars[player.room.name]['itemlist']:
            item_sprites.add(key1)
        elif items['key2'] in roomvars[player.room.name]['itemlist']:
            item_sprites.add(key2)
        elif items['key3'] in roomvars[player.room.name]['itemlist']:
            item_sprites.add(key3)
                

class Exits(pygame.sprite.Sprite):
    
    def __init__(self, (xcord, ycord), image = door):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image = door
        self.rect = self.image.get_rect()
        self.rect.centerx = xcord
        self.rect.centery = ycord

    def imagechanger(self):
        if 'exit' in player.room.name:
            if self == exit1:
                self.image = doorp
            else:
                self.image = door
        return self.image


    def collide(self, rect):
        if self.rect.colliderect(rect):
            collideloc = [ psprite.rect.centery, psprite.rect.centerx ]
            if 6 in roomvars[player.room.name]['exitindex'] and exit1.rect.colliderect(rect):
                psprite.areachange(player.room.name)
            if exit3.rect.colliderect(rect) and 'east' in roomvars[player.room.name]['exits']: # East Exit
                print "east"
                psprite.roomchange(player.room.exits.index('east'), 500 - collideloc[0], collideloc[1] )
            elif exit2.rect.colliderect(rect) and 'west' in roomvars[player.room.name]['exits']: # West Exit
                print "west"
                psprite.roomchange(player.room.exits.index('west'), collideloc[0] + 360, collideloc[1])
            elif exit1.rect.colliderect(rect) and 'south' in roomvars[player.room.name]['exits']: # South Exit
                print "south"
                psprite.roomchange(player.room.exits.index('south'), collideloc[0], 500 - collideloc[1])
            elif exit0.rect.colliderect(rect) and 'north' in roomvars[player.room.name]['exits']: # North Exit
                print "north"
                psprite.roomchange(player.room.exits.index('north'), collideloc[0], collideloc[1] + 360)
            

    def exitsetup(self):
        if 'north' in roomvars[player.room.name]['exits']:
            exit_sprites.add(exit0)
        if 'south' in roomvars[player.room.name]['exits']:
            exit1.imagechanger()
            exit_sprites.add(exit1)
        if 'west' in roomvars[player.room.name]['exits']:
            exit_sprites.add(exit2)
        if 'east' in roomvars[player.room.name]['exits']:
            exit_sprites.add(exit3)


        

def bgupdate(name):
    if name == 'loadscreen':
        background = pygame.image.load('Loadscreen.png')
    elif name == 'background':
        background = pygame.image.load(roomvars[player.room.name]['background'][0])
    elif name == 'puzzleterminal':
        background = pygame.image.load('pic/puzzleterminal.png')
    return background

global reset

def reset():
    background, psprite ,player_sprites, exit_sprites, item_sprites = None, None, None, None, None
    Spritesetter()


def colliding():
    exit0.collide(psprite.rect)
    exit1.collide(psprite.rect)
    exit2.collide(psprite.rect)
    exit3.collide(psprite.rect)
    if items['terminal'] in roomvars[player.room.name]['itemlist']:
        terminal.collide(psprite.rect)
    if items['key1'] in roomvars[player.room.name]['itemlist']:
        key1.collide(psprite.rect)
    if items['key2'] in roomvars[player.room.name]['itemlist']:
        key2.collide(psprite.rect)
    if items['key3'] in roomvars[player.room.name]['itemlist']:
        key3.collide(psprite.rect)

def stuffsetup():
    exit0.exitsetup()
    exit1.exitsetup()
    exit2.exitsetup()
    exit3.exitsetup()
    terminal.itemsetup()
    key1.itemsetup()
    key2.itemsetup()
    key3.itemsetup()

def Spritesetter():
    global player_sprites, exit_sprites, item_sprites, psprite, terminal, key1, key2, key3, exit0, exit1, exit2, exit3, background
    exit0 = Exits(roomvars[player.room.name]['exitlocs'][0])
    exit1 = Exits(roomvars[player.room.name]['exitlocs'][1])
    exit2 = Exits(roomvars[player.room.name]['exitlocs'][2])
    exit3 = Exits(roomvars[player.room.name]['exitlocs'][3])
    psprite = PlayerSprite(250, 250)
    if len(roomvars[player.room.name]['itempos']) != 0:
        terminal = Items('terminal', roomvars[player.room.name]['itempos'][0], roomvars[player.room.name]['itempos'][1])
        key1 = Items('key1', roomvars[player.room.name]['itempos'][0], roomvars[player.room.name]['itempos'][1])
        key2 = Items('key2', roomvars[player.room.name]['itempos'][0], roomvars[player.room.name]['itempos'][1])
        key3 = Items('key3', roomvars[player.room.name]['itempos'][0], roomvars[player.room.name]['itempos'][1])
    player_sprites = pygame.sprite.Group()
    exit_sprites = pygame.sprite.Group()
    item_sprites = pygame.sprite.Group()
    background = bgupdate('background')


# Future Start Screen
##def startscreen():
##    intro = True
##    while intro:
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
##                quit()
##            if event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_ENTER:
##                    intro = False
##        screen.fill(pygame.Color(60, 60, 100))
##        pygame.init()
##        text1 = pygame.font.Font('freesansbold.ttf',115)
##        text2 = pygame.font.Font('freesansbold.ttf',115)
##        TextSurf, TextRect = text_objects("A Game by Jacob Ryans, Diego Prado, Richard Lebell, and Gerard Nelson", text1)
##        TextSurf, TextRect = text_objects("Press Enter to Begin", text2)
##        TextRect2.center = ((display_width/4), (display_height/2))
##        TextRect.center = ((display_width/2),(display_height/2))
##        screen.blit(TextSurf, TextRect)
##        pygame.display.update()
##        pygame.time.delay(900)
##        screen.blit(TextSurf2, TextRect2)
##        pygame.display.update()
##        clock.tick(15)

clock = pygame.time.Clock()
#startscreen()
player = Player(area1.rooms[0])
Spritesetter()

while gamecomplete == False:
    clock.tick(60)
    player_sprites.add(psprite)
    screen.blit(background,(0,0))
    stuffsetup()
    colliding()
    psprite.update()
    player_sprites.draw(screen)
    exit_sprites.draw(screen)
    item_sprites.draw(screen)
    if area1.complete == True and area2.complete == True and area3.complete == True:
        gamecomplete = True
    pygame.display.update()
    root.update()

