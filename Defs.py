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
    global roomvars
    
    areas = {
        'ballground' : {
                'rooms' : [ 6, 6 ],
                'loot' : [ items['testitem'], ],
                'name' : "Ballground"
        },
        'testarea' : {
                'rooms' : [ 6, 6 ],
                'loot' : [ items['testitem'], ],
                'name' : "Foyer"
        }
    }
    
    roomvars = {
        # for exitlocs, its [(north), (south), (east), (west)]
        'testareamain' : {
            'soundtrack' : ['s1'],
            'background' : ['b1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'north', 'south' ],
            'exitindex' : [ 1, 5 ]
        },
        'testarear1' : {
            'soundtrack' : ['s1'],
            'background' : [ 'b1.gif' ],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'east' ],
            'exitindex' : [ 0, 2]
        },
        'testarear2' : {
            'soundtrack' : ['s1'],
            'background' : ['b1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'west', 'north' ],
            'exitindex' : [ 1, 3]
        },
        'testareakeyroom' : {
            'soundtrack' : ['s1'],
            'background' : ['b1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'east' ],
            'exitindex' : [ 2, 4]
        },
        'testarear3' : {
            'soundtrack' : ['s1'],
            'background' : ['b1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'west', 'north' ],
            'exitindex' : [ 3, 5]
        },
        'testareaexit' : {
            'soundtrack' : ['s1'],
            'background' : ['b1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'north' ],
            'exitindex' : [ 4, 0 ]
        }
    }
    
    def __init__(self):
        self.roomvars = roomvars
        self.areas = areas

        
