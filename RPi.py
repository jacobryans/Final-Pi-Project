from Engine import *
from Game import *
import RPi.GPIO as GPIO
from random import randint
import pygame
#declares what switches are used for inputs
switches = [ 23, 18, 24, 25 ]
GPIO.setmode(GPIO.BCM)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# RPi integration file (In the works)

try:

    while(True):
        if(GPIO.input(switches[0]) == True):
            print "north"
            
        elif(GPIO.input(switches[1]) == True):
            print "south"
            
        elif(GPIO.input(switches[2]) == True):
            print "east"
            
        elif(GPIO.input(switches[3]) == True):
            print "west"
            
        else:
            print "nothing detected.."
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    
