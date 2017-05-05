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
screen.blit(d, (playerx, playery))
#screen.blit(d, (playerx, playery))
pygame.display.init()
pygame.display.update()
def draw():
    #pygame.draw.circle(screen, (0,0,0), (250,250), 125)
    #pygame.display.update()
    #button1 = Button(buttonwin,text = 'Draw',  command=draw)
    #button1.pack(side=LEFT)
    root.update()

def detection():
    for event in pygame.event.get():
        global playerx, playery
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print "left"
                playerx -= 10
                pic = r
                screen.blit(pic1, (0, 0))
                screen.blit(pic, (playerx, playery))
            elif event.key == pygame.K_RIGHT:
                print "right"
                playerx += 10
                pic = l
                screen.blit(pic1, (0, 0))
                screen.blit(pic, (playerx, playery))
            elif event.key == pygame.K_UP:
                print "up"
                playery -= 10
                pic = u
                screen.blit(pic1, (0, 0))
                screen.blit(pic, (playerx, playery))
            elif event.key == pygame.K_DOWN:
                print "down"
                playery += 10
                pic = d
                screen.blit(pic1, (0, 0))
                screen.blit(pic, (playerx, playery))
        

while True:
    pic = detection()
    pygame.display.update()
    root.update()      
