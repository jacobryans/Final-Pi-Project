from Defs import *
import pygame
from random import randint, choice

global directions, inverse
directions = [ "north", "south", "west", "east" ]
inverse = {
        "south" : "north",
        "north" : "south",
        "west" : "east",
        "east" : "west"
        }

class Area(object):
    
    def __init__(self, name, complete=False):
        global info
        info = MapDefs()
        self.area = info.areas[name]
        self.complete = complete
        # set all of these to a default list value
        self.name = name
        self.rooms, self.enemies = [], []
        self.max = randint(self.area["rooms"][0], self.area["rooms"][1]) # set the max amount of rooms, for us to index
        # add all the rooms, by spawning Room()s

    def __str__(self):
        s = self.name
        return s

    def rooms(self, value=None):
        if(value == None):
            return self._rooms
        self._rooms = value
        
    def name(self, value=None):
        if (value == None):
            return self._name
        self._name = value
    
    def max(self, value=None):
        if (value == None):
            return self._max
        self._name = value
    
    def addRoom(self, room):
        self.rooms.append(room)

    def area(self, value=None):
        if (value == None):
            return self._area
        self._area = value
        
    def setupRooms(self):
        global roomtypes
        roomtypes = [ 'main', 'r1', 'r2', 'keyroom', 'r3', 'exit' ]
        original, limit, elimit = None, -1, -1
        room = None
        # add all rooms to the list
        for i in range(self.max):
            # Creates a room object with the roomtype string
            room = Room(self.name + str(roomtypes[i]))
            # Adds the room to the area
            self.addRoom(room)
        for i in range(self.max):
            # Sets limit and elimit to 0, n is set to a room for easy room access
            limit += 1
            n = self.rooms[limit]
            elimit = -1
            while len(roomvars[self.name + roomtypes[limit]]['exits']) != elimit+1:
                # If there is only 1 exit, don't bother with going through the whole loop
                if len(roomvars[self.name + roomtypes[limit]]['exitindex']) == 1:
                    ri = roomvars[self.name + roomtypes[limit]]['exitindex'][elimit]
                    exit = roomvars[self.name + roomtypes[limit]]['exits'][elimit]
                    aname = self
                    n.addExit(ri, exit, aname)
                    break
                elimit += 1
                # There are wierd exceptions with the end room going to the next area, so an innefficient solution is used :(
                if roomtypes[limit] == 'exit' and self.name == 'area1':
                    n.addExit(0, 'south', area1)
                    n.addExit(1, 'east', area1)
                    n.addExit(4, 'north', area1)
                    break
                elif roomtypes[limit] == 'exit' and self.name == 'area2':
                    n.addExit(0, 'south', area2)
                    n.addExit(1, 'east', area2)
                    break
                elif roomtypes[limit] == 'exit' and self.name == 'area3':
                    n.addExit(4, 'north', area3)
                    n.addExit(0, 'south', area3)
                    # If the room isn't an exit room, appends an exit based on the roomindex, exit, and the area name
                else:
                    ri = roomvars[self.name + roomtypes[limit]]['exitindex'][elimit]
                    exit = roomvars[self.name + roomtypes[limit]]['exits'][elimit]
                    aname = self
                    n.addExit(ri, exit, aname)
                
            
class Room(object):
    # Simple room object class
    def __init__(self, name):
        self.name = name
        # Exits are exits
        self.exits = []
        # Locations are the rooms connected to the exit in index
        self.locations = []

    # String representer, used for debugging mainly
    def __str__(self):
        s = str(self.name)
        s += "\n"
        s += str(self.exits)
        s += "\n"
        s += str(self.locations)
        return s

    # Setters and getters
    def locations(self, value=None):
        if (value == None):
            return self._locations
        self._locations = value

    def exits(self, value=None):
        if (value == None):
            return self._exits
        self._exits = value

    # Item function that adds items to room, not implemented
    def doItem(self, item, remove=False):
        if(remove == False):
                self.items.append(item)
        else:
                self.items.remove(item)

    # adds an exit to the room, the exit is a string (e.g., north), the room is an instance of a room
    def addExit(self, ri, exit, aname):
        if ri!= 6:
            self.exits.append(exit)
            self.locations.append(aname.rooms[ri])

    # Function created for a more dynamic exit system, to be later implemented    
    # boolean, used to check if there is an exit in a direction
    def checkExit(self, direction):
        # check for valid exits in the current room
        for i in range(len(self.exits)): # this exits index exists in the array
            if (direction == self.exits[i]): # check if it matches our direction
                return True
                break
        return False
    
class Item(object):
    # Item object class, not fully implemented but will be used with tkinter in future development
    def __init__(self, name):
        self.name = name
        item = ItemDefs()
        self.desc = item.items[str(name)]['desc']
        self.type = item.items[str(name)]['type']
        self.key = item.items[str(name)]['key']

    # String representation of item, used for debugging
    def __str__(self):
        s = "Item string test"
        s += "\n"
        s += str(self.desc)
        s += "\n"
        s += str(self.type)
        s += "\n"
        s += str(self.key)
        return s
    
    def name(self, value=None):
        if(value == None):
            return self._name
        self._name = value
        
    def desc(self, value=None):
        if(value == None):
            return self._desc
        self._desc = value
        
    def type(self, value=None):
        if(value == None):
            return self._type
        self._type = value
        
    def key(self, value=None):
        if(value == None):
            return self._key
        self._key = value


# Initializes the areas and sets them up with rooms and such
global area1, area2, area3
area1, area2, area3 = Area('area1'), Area('area2'), Area('area3')
area1.setupRooms()
area2.setupRooms()
area3.setupRooms()
