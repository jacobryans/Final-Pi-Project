class MapDefs:
    global areas
    
    areas = {
        "Old Town" : {
                "rooms" : [ rooms["testroom"],  ],
                "loot" : [  ]
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
