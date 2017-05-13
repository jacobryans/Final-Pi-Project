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
            room = Room(self.name + str(roomtypes[i]))
            self.addRoom(room)
        for i in range(self.max):
            limit += 1
            n = self.rooms[limit]
            elimit = -1
            while len(roomvars[self.name + roomtypes[limit]]['exits']) != elimit+1:
                if len(roomvars[self.name + roomtypes[limit]]['exitindex']) == 1:
                    ri = roomvars[self.name + roomtypes[limit]]['exitindex'][elimit]
                    exit = roomvars[self.name + roomtypes[limit]]['exits'][elimit]
                    aname = self
                    n.addExit(ri, exit, aname)
                    break
                #if len(n.exits) < 3 and elimit == 1:
                    #elimit -=1
                #if len(n.exits) == 3 and elimit == 2:
                    #ellimit -= 1
                elimit += 1
                if roomtypes[limit] == 'exit' and self.name == 'area1' and elimit == 2:
                    n.addExit(0, 'south', area1)
                elif roomtypes[limit] == 'exit' and self.name == 'area2' and elimit == 1:
                    n.addExit(0, 'south', area2)
                elif roomtypes[limit] == 'exit' and self.name == 'area3' and elimit == 1:
                    n.addExit(0, 'south', area3)
                else:
                    ri = roomvars[self.name + roomtypes[limit]]['exitindex'][elimit]
                    exit = roomvars[self.name + roomtypes[limit]]['exits'][elimit]
                    aname = self
                    n.addExit(ri, exit, aname)
                
            
class Room(object):
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.locations = []
        self.items = []
        self.usables = []

    def __str__(self):
        s = str(self.name)
        s += "\n"
        s += str(self.exits)
        s += "\n"
        s += str(self.locations)
        return s
    
    def items(self, value=None):
        if (value == None):
            return self._items
        self._items = value
        
    def usables(self, value=None):
        if (value == None):
            return self._usables
        self._usables = value
    
    def locations(self, value=None):
        if (value == None):
            return self._locations
        self._locations = value

    def exits(self, value=None):
        if (value == None):
            return self._exits
        self._exits = value

    def doItem(self, item, remove=False):
        if(remove == False):
                self.items.append(item)
        else:
                self.items.remove(item)

    # adds an exit to the room, the exit is a string (e.g., north), the room is an instance of a room
    def addExit(self, ri, exit, aname): # append the exit and room to the appropriate lists
        self.exits.append(exit)
        self.locations.append(aname.rooms[ri])
        # add room exits on the opposite side
        #self.exits.append(inverse[exit])
        #self.locations.append(aname.rooms[ri-1])
    
    # boolean, used to check if there is an exit in a direction
    def checkExit(self, direction):
        # check for valid exits in the current room
        for i in range(len(self.exits)): # this exits index exists in the array
            if (direction == self.exits[i]): # check if it matches our direction
                return True
                break
        return False
    
class Item(object):
    def __init__(self, name):
        self.name = name
        item = ItemDefs()
        self.desc = item.items[str(name)]['desc']
        self.type = item.items[str(name)]['type']
        self.key = item.items[str(name)]['key']

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

global area1, area2, area3
area1, area2, area3 = Area('area1'), Area('area2'), Area('area3')
area1.setupRooms()
area2.setupRooms()
area3.setupRooms()
