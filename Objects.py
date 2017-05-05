from Defs import *
from pygame import *
from random import *

global directions, inverse
directions = [ "north", "south", "west", "east" ]
inverse = {
        "south" : "north",
        "north" : "south",
        "west" : "east",
        "east" : "west"
        }
        
    
class Area(object):
    
    def __init__(self, name):
        self.name = name
        global info
        info = MapDefs()
        self.rooms = []
        self.area = info.areas[name]
        self.items = self.area['loot']
        self.max = randint(self.area["rooms"][0], self.area["rooms"][1])

    def __str__(self):
        s = "You are in the game. "
        s += "\n"
        s += "You are in the "
        s += info.areas[self.name]['name']
        s += " area."
        return s

    def items(self, value=None):
        if(value == None):
            return self._items
        self._items = value

    def rooms(self, value=None):
        if(value == None):
            return self._rooms
        self._rooms = value
        
    def name(self, value=None):
        if value == None:
            return self._name
        self._name = value
    
    def max(self, value=None):
        if value == None:
            return self._max
        self._name = value
    
    def addRoom(self, room):
        self.rooms.append(room)
    
    def setupRooms(self):
        first, golden, original, limit = False, False, None, 0
        room = None
        # add all rooms to the list
        for i in range(self.max+1):
            golden = (first == False) & ((randint(0, 4) == 0) or i == (self.max+1))
            if(golden == True):
                first = True
            room = Room(golden)
            self.addRoom(room)
            room.doItem(choice(self.items))
        # setup each room with exits, use index to track first room
        for i in range(self.max+1):
            if(i < limit):
                i = limit
            if(limit < self.max+1): # we can decrement the amount of rooms to get an accurate number
                room = self.rooms[i] # easily accessible room object 
                direction = directions[randint(0, 3)] # our current direction for the default new room
                while room.checkExit(direction): # makes sure we get a good direction
                    original = direction # this gets set to re-add it later
                    directions.remove(original)
                    direction = directions[randint(0, 2)]
                    directions.remove(direction)
                limit = i+1 # set new limit
                if(limit < self.max+1): # new default extra room
                    room.addExit(direction, self.rooms[limit])
                    
                if(randint(0, 2) == 0): # random added room 
                    if(limit < self.max):
                        limit += 1 # increment by one
                        room.addExit(directions[len(directions)-1], self.rooms[limit])
                directions.append(direction)
                if(original != None):
                    directions.append(original)
            else:
                break
            
class Room(object):
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.locations = []
        self.items = []
        self.usables = []

    def __str__(self):
        s = "You are in a room"
        s += "\n"
        s += self.name
        s += "\n"
        return s
        
    def name(self, value=None):
        if value == None:
            return self._name
        self._name = value
    
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
    def addExit(self, exit, room): # append the exit and room to the appropriate lists
        self.exits.append(exit)
        self.locations.append(room)
        # add room exits on the opposite side
        self.exits.append(inverse[exit])
        self.locations.append(self)
    
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
    
    def stats(self, value=None):
        if(value == None):
            return self._stats
        self._stats = value
