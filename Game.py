import os
import sys
import time
import inputbox
import ctypes
from pygame import *
import Tkinter as tk
from Tkinter import *
from Objects import *
from Defs import MapDefs

directions = [ 'north','south','west','east']

# Setting up the interface
root = tk.Tk() # Setting up tkinter
embed = tk.Frame(root, width = 500, height = 500) #creates embed frame for pygame window
embed.grid(columnspan = (500), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
buttonwin = tk.Frame(root, width = 0, height = 500) # Button for tkinter
buttonwin.pack(side = LEFT)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
screen = pygame.display.set_mode((500,500)) # Pygame setdisplay
screen.fill(pygame.Color(60,60,100)) #Fills with a color
global d, l, r, u, door, doorp, loadscreen #setting global picture vars
loadscreen = pygame.image.load('Loadscreen.png')
d = ['pic/down1.png','pic/down2.png','pic/down3.png', 'pic/down4.png'] # buffer for each direction for animated walking (working on this)
l = ['pic/left1.png','pic/left2.png','pic/left3.png', 'pic/left4.png']
r = ['pic/right1.png','pic/right2.png','pic/right3.png', 'pic/right4.png']
u = ['pic/up1.png','pic/up2.png','pic/up3.png', 'pic/up4.png']
door = pygame.image.load('pic/door.png')
doorp = pygame.image.load('pic/doorp.png')
gamecomplete = None # setting variables
loading = None
pygame.display.init()
pygame.display.update()


# Player class, handles the player's room and can add other functionalitys
class Player(object):
    def __init__(self, room, first):
        self.room = room
        self.first = first
    
    def room(self, value=None):
        if (value == None):
            return self._room
        self._room = value

    def first(self, value=None):
        if (value == None):
            return self._first
        self._first = value

# Playersprite class, handles the visual player qualities
class PlayerSprite(pygame.sprite.Sprite):
    
    def __init__(self, px ,py):
        # Initializing the sprite and its rect
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((px, py))
        self.image = pygame.image.load('pic/up1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = px
        self.rect.centery = py

    # Setters and getters
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


    # This moves the player when called, sets FPS at 60 and changes the player rect and its images, also used for debugging and checking of player coords
    # So the player doesn't walk out of bounds
    def update(self):
        clock.tick(60)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
                self.image = pygame.image.load(l[0])
                self.rect.centerx -= 3
                self.image = pygame.image.load(l[1])
                self.rect.centerx -= 3
                self.image = pygame.image.load(l[2])
                self.rect.centerx -= 3
                self.image = pygame.image.load(l[3])
                self.rect.centerx -= 3
        if keystate[pygame.K_RIGHT]:
                self.image = pygame.image.load(r[0])
                self.rect.centerx += 3
                self.image = pygame.image.load(r[1])
                self.rect.centerx += 3
                self.image = pygame.image.load(r[2])
                self.rect.centerx += 3
                self.image = pygame.image.load(r[3])
                self.rect.centerx += 3
        if keystate[pygame.K_UP]:
                self.image = pygame.image.load(u[0])
                self.rect.centery -= 3
                self.image = pygame.image.load(u[1])
                self.rect.centery -= 3
                self.image = pygame.image.load(u[2])
                self.rect.centery -= 3
                self.image = pygame.image.load(u[3])
                self.rect.centery -= 3
        if keystate[pygame.K_DOWN]:
                self.image = pygame.image.load(d[0])
                self.rect.centery += 3
                self.image = pygame.image.load(d[1])
                self.rect.centery += 3
                self.image = pygame.image.load(d[2])
                self.rect.centery += 3
                self.image = pygame.image.load(d[3])
                self.rect.centery += 3
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

    # Changes the player room
    def roomchange(self, index):
            # Sets loading to true so we have an accurate load everytime
            loading = True
            while loading == True:
                # Changes the player's room
                player.room = player.room.locations[index]
                # Brings up the loadscreen
                screen.blit(loadscreen, (0, 0))
                # Updates the display
                pygame.display.update()
                # Delays time for visual pleasing
                pygame.time.delay(2000)
                # Sets player rect location
                pygame.display.update()
                pygame.time.delay(3000)
                # Resets the player and all other sprites etc.
                reset()
                pygame.display.update()
                # Sets loading to false to break out of loop
                loading = False

    # Changes the player's area after completing the puzzle and walking thru the portal
    def areachange(self, room):
        # Loading = true for same reason as roomchange
        loading = True
        while loading == True:
            # Checks the player's area and completion of the area
            if player.room.name == 'area1exit' and area1.complete == True:
                # Sets area and room based on current location
                player.area = area2
                player.room = area2.rooms[0]
                # Brings up loadscreen
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                # Delays for a second to mimic loading
                pygame.time.delay(3000)
                # Draws the player to the screen
                player_sprites.draw(screen)
                # Resets
                reset()
                # Updates the display
                pygame.display.update()
                # Breaks out of loop
                loading = False
            elif player.room.name == 'area2exit' and area2.complete == True:
                player.area = area3
                player.room = area3.rooms[0]
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                pygame.time.delay(3000)
                player_sprites.draw(screen)
                reset()
                pygame.display.update()
                loading = False
            elif player.room.name == 'area3exit' and area3.complete == True:
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                pygame.time.delay(3000)
                player_sprites.draw(screen)
                reset()
                pygame.display.update()
                loading = False
            else:
                reset()
                loading = False

# Used for random sprites not categorized to an exit, player, or item (Mainly UI thing)
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
        # Sets up the item sprite, including the type, key, and desc
        self.image = pygame.Surface((50, 40))
        self.image = pygame.image.load(items[self.name]['pic'][0])
        self.rect = self.image.get_rect()
        self.rect.centerx = px
        self.rect.centery = py
        self.type = items[self.name]['type']                        
        self.key = items[self.name]['key']
        self.desc = items[self.name]['desc']

    def collide(self, rect):
        # Checks for collision, and decides a route of code based on the collision
        if self.rect.colliderect(psprite.rect):
            # If the collided item is the terminal
            if self == terminal:
                # We use termcollide so we can break out of the recursion with L_SHIFT
                termcollide = True
                while termcollide == True:
                    if player.room.name == 'area1r1':
                        # Checks the area above and then intializes a sprite, spritegroup, and adds the sprite to the group and draws it
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
                    # This is used to handle player input to get out of the screen
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LSHIFT:
                                reset()
                                termcollide = False
                                break
            # Checks to see if self.key == True and checks the name of the item, then uses inputbox to record player input
            elif self.key == True:
                if self.name == 'key1':
                    # Fills the screen to overlay the other sprites
                    screen.fill((0,0,0))
                    answer = inputbox.ask(screen, "Answer: ")
                    reset()
                    if answer == 'theanswertoallanswers':
                        ctypes.windll.user32.MessageBoxA(0, "Admin Status Approved. Continue to next area.", "HACKED.OUT", 1)
                        area1.complete = True
                    else:
                        ctypes.windll.user32.MessageBoxA(0, "Admin Status Negated. Find the terminal for a hint.", "HACK.FAIL", 1)
                        area1.complete = False
                elif self.name == 'key2':
                    screen.fill((0,0,0))
                    answer = inputbox.ask(screen, "Answer: ")
                    reset()
                    if a2puzzle == '15':
                        ctypes.windll.user32.MessageBoxA(0, "Admin Status Approved. Continue to next area.", "HACKED.OUT", 1)
                        area2.complete = True
                    else:
                        ctypes.windll.user32.MessageBoxA(0, "Admin Status Negated. Find the terminal for a hint.", "HACK.FAIL", 1)
                        area2.complete = False
                elif self.name == 'key3':
                    screen.fill((0,0,0))
                    answer = inputbox.ask(screen, "Answer: ")
                    reset()
                    if a3puzzle == '20':
                        ctypes.windll.user32.MessageBoxA(0, "Admin Status Approved. Continue to next area.", "HACKED.OUT", 1)
                        area3.complete = True
                    else:
                        ctypes.windll.user32.MessageBoxA(0, "Admin Status Negated. Find the terminal for a hint.", "HACK.FAIL", 1)
                        area3.complete = False
            
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
                
# Class for handling exits and their sprites
class Exits(pygame.sprite.Sprite):
    
    def __init__(self, (xcord, ycord), image = door):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image = door
        self.rect = self.image.get_rect()
        self.rect.centerx = xcord
        self.rect.centery = ycord

    def imagechanger(self):
        # simple function for changing the portal color if it leads to another area
        if 'exit' in player.room.name:
            if self == exit1:
                self.image = doorp
            else:
                self.image = door
        return self.image


    def collide(self, rect):
        # Checks collision with exit
        if self.rect.colliderect(rect):
            # Records collide location of player and sets appropriate next room spawn
            x_mod, y_mod = 0, 0
            if 6 in roomvars[player.room.name]['exitindex'] and exit1.rect.colliderect(rect):
                psprite.areachange(player.room.name)
            if exit3.rect.colliderect(rect) and 'east' in roomvars[player.room.name]['exits']: # East Exit
                print "east"
                psprite.roomchange(player.room.exits.index('east'))
            elif exit2.rect.colliderect(rect) and 'west' in roomvars[player.room.name]['exits']: # West Exit
                print "west"
                psprite.roomchange(player.room.exits.index('west'))
            elif exit1.rect.colliderect(rect) and 'south' in roomvars[player.room.name]['exits']: # South Exit
                print "south"
                psprite.roomchange(player.room.exits.index('south'))
            elif exit0.rect.colliderect(rect) and 'north' in roomvars[player.room.name]['exits']: # North Exit
                print "north"
                psprite.roomchange(player.room.exits.index('north'))
            

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

# Initialize clock (for fps)
clock = pygame.time.Clock()
#startscreen()
# Sets up player instance
player = Player(area1.rooms[0], True)
# Sets up all sprites
Spritesetter()

while gamecomplete != True:
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

