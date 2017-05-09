from Objects import *
from Game import *
from Defs import MapDefs
        

class Engine:
    def Interact(self):
        pass

    def roomchange(self, index):
        while load == True:
            screen.blit(loadscreen, (0,0))
            currentRoom = p.room.locations[index]
            if directions[0] in currentRoom.exits:
                # can add more load features here
                # this just blits exits around the room based on roomtype and the coords from the dictionary
                screen.blit(l, roomvars[str(currentRoom.name)]['exitlocs'][0])
                
            if directions[1] in currentRoom.exits:
                screen.blit(l, roomvars[str(currentRoom.name)]['exitlocs'][1])
                
            if directions[2] in currentRoom.exits:
                screen.blit(l, roomvars[str(currentRoom.name)]['exitlocs'][2])
                
            if directions[3] in currentRoom.exits:
                screen.blit(l, roomvars[str(currentRoom.name)]['exitlocs'][3])
                
            load = False
                             
    def Process(self):
        pass





