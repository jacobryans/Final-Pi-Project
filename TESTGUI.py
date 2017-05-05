import pygame
import Tkinter as tk
from Tkinter import *
import os

root = tk.Tk()
embed = tk.Frame(root, width = 500, height = 500) #creates embed frame for pygame window
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
buttonwin = tk.Frame(root, width = 75, height = 500)
buttonwin.pack(side = LEFT)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
playerx = 250
playery = 250
screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color(60,60,100))
pic1 = pygame.image.load('Background.gif')
d = pygame.image.load('1.png')
r = pygame.image.load('2.png')
l = pygame.image.load('3.png')
u = pygame.image.load('4.png')
screen.blit(pic1, (0, 0))
#screen.blit(d, (playerx, playery))
pygame.display.init()
pygame.display.update()
def draw():
    #pygame.draw.circle(screen, (0,0,0), (250,250), 125)
    #pygame.display.update()
    #button1 = Button(buttonwin,text = 'Draw',  command=draw)
    #button1.pack(side=LEFT)
    root.update()

while True:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        print "nignog"
        playerx -= 10
    elif pressed[pygame.K_RIGHT]:
        print "nignog"
        playerx += 10
    elif pressed[pygame.K_DOWN]:
        print "nignog"
        playery -= 10
    elif pressed[pygame.K_UP]:
        print "nignog"
        playery += 10
    screen.blit(u, (playerx, playery))
    pygame.display.update()
    root.update()      
