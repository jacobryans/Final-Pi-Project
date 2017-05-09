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

    roomvars = {
        # for exitlocs, its [(north), (south), (east), (west)]
        'main' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200)]
        },
        'r1' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200)]
        },
        'r2' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200)]
        },
        'r3' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200)]
        },
        'key' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200)]
        },
        'r4' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200)]
        },
        'r5' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200)]
        },
        'r6' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200)]
        },
        'exit' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200)]
        }
    }
    
    def __init__(self):
        self.roomvars = roomvars
        self.areas = areas

        
