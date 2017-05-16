
# Huge import list, gotta love it.
import os
import sys
import time
import inputbox
import ctypes
import pygame
from pygame import *
import Tkinter as tk
from Tkinter import *
from Objects import *
from Defs import MapDefs


# Setting up the interface
root = tk.Tk() # Setting up tkinter
embed = tk.Frame(root, width = 500, height = 500) #creates embed frame for pygame window
embed.grid(columnspan = (500), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
buttonwin = tk.Frame(root, width = 0, height = 500) # Button for tkinter
buttonwin.pack(side = LEFT)

# Setting up SDL window so that tkinter can be used with pygame
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
screen = pygame.display.set_mode((500,500)) # Pygame setdisplay
screen.fill(pygame.Color(60,60,100)) #Fills with a color

# Setting global picture vars
global d, l, r, u, door, doorp, loadscreen
loadscreen = pygame.image.load('pic/Loadscreen.png')
d = ['pic/down1.png','pic/down2.png','pic/down3.png', 'pic/down4.png'] # buffer for each direction for animated walking (working on this)
l = ['pic/left1.png','pic/left2.png','pic/left3.png', 'pic/left4.png']
r = ['pic/right1.png','pic/right2.png','pic/right3.png', 'pic/right4.png']
u = ['pic/up1.png','pic/up2.png','pic/up3.png', 'pic/up4.png']
door = pygame.image.load('pic/door.png')
doorp = pygame.image.load('pic/doorp.png')

# Initializing variables
gamecomplete = None 
loading = None
pygame.mixer.init()
pygame.mixer.music.load("music/loz_ost.wav")
pygame.mixer.music.play(0)
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
    # So the player doesn't walk out of bounds. The movement is being worked on, sorry about the inefficiency
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
                pygame.time.delay(500)
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
                player.room = area2.rooms[0]
                # Brings up loadscreen
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                musicchange()
                pygame.mixer.music.play(0)
                # Delays for a second to mimic loading
                pygame.time.delay(1000)
                # Draws the player to the screen
                player_sprites.draw(screen)
                # Resets
                reset()
                # Updates the display
                pygame.display.update()
                # Breaks out of loop
                loading = False
            elif player.room.name == 'area2exit' and area2.complete == True:
                player.room = area3.rooms[0]
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                musicchange()
                pygame.mixer.music.play(0)
                pygame.time.delay(1000)
                player_sprites.draw(screen)
                reset()
                pygame.display.update()
                loading = False
            elif player.room.name == 'area3exit' and area3.complete == True:
                # When the game is complete
                screen.blit(loadscreen, (0, 0))
                pygame.display.update()
                pygame.time.delay(1000)
            else:
                reset()
                loading = False

global musicchange

def musicchange():
    pygame.mixer.music.load(roomvars[player.room.name]['soundtrack'][0])
    pygame.mixer.music.play(0)


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
                    elif player.room.name == 'area2exit':
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
                    # Brings up the inputbox, and queries for an answer
                    answer = inputbox.ask(screen, "Answer: ")
                    # Resets the screen when answer is inputted
                    reset()
                    # If the answer is correct, you'll get confirmation, if it isn't, you get confirmation you suck. Area is set to complete or not complete
                    if answer == 'theanswertoallanswers':
                        # Ctypes is a python library used for notification messages
                        ctypes.windll.user32.MessageBoxA(0, "Admin Status Approved. Continue to next area.", "HACKED.OUT", 1)
                        area1.complete = True
                    else:
                        ctypes.windll.user32.MessageBoxA(0, "Admin Status Negated. Find the terminal for a hint.", "HACK.FAIL", 1)
                        area1.complete = False
                elif self.name == 'key2':
                    screen.fill((0,0,0))
                    answer = inputbox.ask(screen, "Answer: ")
                    reset()
                    if answer == '0':
                        ctypes.windll.user32.MessageBoxA(0, "Admin Status Approved. Continue to next area.", "HACKED.OUT", 1)
                        area2.complete = True
                    else:
                        ctypes.windll.user32.MessageBoxA(0, "Admin Status Negated. Find the terminal for a hint.", "HACK.FAIL", 1)
                        area2.complete = False
                elif self.name == 'key3':
                    screen.fill((0,0,0))
                    answer = inputbox.ask(screen, "Answer: ")
                    reset()
                    if answer == 'thedankanky':
                        ctypes.windll.user32.MessageBoxA(0, "H38ks81 Error. PLAYER HAS COMPLETE CONTROL OF SYSTEM.", "TOU.DEKCAH", 1)
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
        # Sets up the exit sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image = door
        self.rect = self.image.get_rect()
        self.rect.centerx = xcord
        self.rect.centery = ycord

    def imagechanger(self):
        # simple function for changing the portal color if it leads to another area
        if roomvars[player.room.name]['exitindex'][0] == 6:
            if self == exit1:
                exit1.image = doorp
        else:
            self.image = door
        return self.image


    def collide(self, rect):
        # Checks collision with exit
        if self.rect.colliderect(rect):
            # Checks different situations to see if the player is traversing rooms
            # The first statement checks to see if there is an area exit, and if it is the south exit
            if roomvars[player.room.name]['exitindex'][0] == 6 and exit1.rect.colliderect(rect):
                # Passes in the player name and calls changeroom
                psprite.areachange(player.room.name)
            # Checks for all  of exit collides
            # Directions go as follows- (0-north)(1-south)(2-west)(3-east)
            if exit3.rect.colliderect(rect) and 'east' in roomvars[player.room.name]['exits']: # East Exit
                psprite.roomchange(player.room.exits.index('east'))
            elif exit2.rect.colliderect(rect) and 'west' in roomvars[player.room.name]['exits']: # West Exit
                psprite.roomchange(player.room.exits.index('west'))
            elif exit1.rect.colliderect(rect) and 'south' in roomvars[player.room.name]['exits']: # South Exit
                psprite.roomchange(player.room.exits.index('south'))
            elif exit0.rect.colliderect(rect) and 'north' in roomvars[player.room.name]['exits']: # North Exit
                psprite.roomchange(player.room.exits.index('north'))
            

    def exitsetup(self):
        # Sets up exits based on current directions in room
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
    # Updates the background based on what name is passed in
    if name == 'loadscreen':
        background = pygame.image.load('pic/Loadscreen.png')
    elif name == 'background':
        background = pygame.image.load(roomvars[player.room.name]['background'][0])
    return background


global reset


def reset():
    # Resets these variables so there are no replicates
    background, psprite ,player_sprites, exit_sprites, item_sprites = None, None, None, None, None
    Spritesetter()

global finishgame


def finishgame():
    # End of game handler
    gamecomplete = True
    while gamecomplete == True:
        background = pygame.image.load('pic/Finishscreen.png')
        screen.blit(background, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
def colliding():
    # Collide function for exits and items, we check all exit collides since area exits have no direction, atleast there are exceptions
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
    # Just sets up all items
    exit0.exitsetup()
    exit1.exitsetup()
    exit2.exitsetup()
    exit3.exitsetup()
    terminal.itemsetup()
    key1.itemsetup()
    key2.itemsetup()
    key3.itemsetup()


def Spritesetter():
    # Setting globals so they can be called anywhere in the file. There are no replicates of these.
    global player_sprites, exit_sprites, item_sprites, psprite, terminal, key1, key2, key3, exit0, exit1, exit2, exit3, background
    # Initializing exit objects
    exit0 = Exits(roomvars[player.room.name]['exitlocs'][0])
    exit1 = Exits(roomvars[player.room.name]['exitlocs'][1])
    exit2 = Exits(roomvars[player.room.name]['exitlocs'][2])
    exit3 = Exits(roomvars[player.room.name]['exitlocs'][3])
    # Initializing playersprite object
    psprite = PlayerSprite(250, 250)
    # Checks to see if there is even an item in the room, then adds the items
    if len(roomvars[player.room.name]['itempos']) != 0:
        terminal = Items('terminal', roomvars[player.room.name]['itempos'][0], roomvars[player.room.name]['itempos'][1])
        key1 = Items('key1', roomvars[player.room.name]['itempos'][0], roomvars[player.room.name]['itempos'][1])
        key2 = Items('key2', roomvars[player.room.name]['itempos'][0], roomvars[player.room.name]['itempos'][1])
        key3 = Items('key3', roomvars[player.room.name]['itempos'][0], roomvars[player.room.name]['itempos'][1])
    # Sets up the sprite groups for adding sprites into
    player_sprites = pygame.sprite.Group()
    exit_sprites = pygame.sprite.Group()
    item_sprites = pygame.sprite.Group()
    # Sets the background
    background = bgupdate('background')

# Initial game settings that need to be updated
# Initialize clock (for fps)
clock = pygame.time.Clock()
# Sets up player instance
player = Player(area1.rooms[0], True)
# Sets up all sprites
Spritesetter()

# Game loop while the game isn't completed by the player
while gamecomplete != True:
    #FPS setting
    clock.tick(60)
    #Adding the player sprite
    player_sprites.add(psprite)
    #Blitting the background
    screen.blit(background,(0,0))
    # Chooses the music through the roomvars dic
    #Sets up the exits and the items by checking if they're in the room
    stuffsetup()
    #Checks to see if the player collides with any collidables
    colliding()
    #Checks for player movement
    psprite.update()
    #Draws all sprites to the screen
    player_sprites.draw(screen)
    exit_sprites.draw(screen)
    item_sprites.draw(screen)
    #Checks to see if all areas are complete yet
    if psprite.rect.colliderect(exit1.rect) and player.room.name == "area3exit" and area1.complete == True and area2.complete == True and area3.complete == True:
        finishgame()
    #Updates the display and tkinter UI
    pygame.display.update()
    root.update()

