class MapDefs:
    global areas
    
    areas = {
        "Old Town" : {
                "rooms" : [ 5, 7 ],
                "enemies" : [ "goblin", "zombie", "fox", "ghost", "barbarian" ],
                "loot" : [ "potion", "rope", "homestone" ],
                "boss" :  "troll"
        },
    }
    
    def __init__(self):
        self.areas = areas

class ItemDefs:
    global items

    items = {
        "testitem" : {
            "type" : usable,
            "key" : True,
            "desc" : "A Test Item"
            },
        }

    def __init__(self):
        self.items = items
        
class RoomDefs:
    global rooms

    rooms = {
        "testroom" : {
            "locked" : False,
            "background" : "pic1",
            "items" : items["testitem"],
            "desc" : "A Test Room"
            }
            
    def __init__(self):
        self.rooms = rooms
