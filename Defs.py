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
            'exitlocs' : [(0, 0), (100, 100), (200, 200), (300, 300)]
        },
        'r1' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200), (300, 300)]
        },
        'r2' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200), (300, 300)]
        },
        'r3' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200), (300, 300)]
        },
        'key' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200), (300, 300)]
        },
        'r4' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200), (300, 300)]
        },
        'r5' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200), (300, 300)]
        },
        'r6' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200), (300, 300)]
        },
        'exit' : {
            'soundtracks' : ['s1', 's2', 's3', 's4'],
            'backgrounds' : ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'],
            'exitlocs' : [(0, 0), (100, 100), (200, 200), (300, 300)]
        }
    }
    
    def __init__(self):
        self.roomvars = roomvars
        self.areas = areas

        
