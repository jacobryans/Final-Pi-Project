class ItemDefs:
    global items

    items = {
        'testitem' : {
            'type' : 'usable',
            'key' : True,
            'desc' : 'A Test Item'
            },
        }

    def __init__(self):
        self.items = items


class MapDefs:
    global areas
    
    areas = {
        'ballground' : {
                'rooms' : [ 5, 7 ],
                'loot' : [ items['testitem'], ],
                'name' : "Ballground"
        },
        'testarea' : {
                'rooms' : [ 5, 7 ],
                'loot' : [ items['testitem'], ],
                'name' : "Foyer"
        }
    }
    
    def __init__(self):
        self.areas = areas

        
