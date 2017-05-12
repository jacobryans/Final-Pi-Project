class ItemDefs:
    global items

    items = {
        'terminal' : {
            'type' : 'usable',
            'pic' : '1.gif',
            'key' : False,
            'desc' : 'Informational Terminal'
            },
        'key1' : {
            'type' : 'read',
            'pic' : '2.gif',
            'key' : True,
            'desc' : 'Key Item for Area 1'
            },
        'key2' : {
            'type' : 'read',
            'pic' : '3.gif',
            'key' : True,
            'desc' : 'Key Item for Area 2'
            },
        'key3' : {
            'type' : 'read',
            'pic' : '4.gif',
            'key' : True,
            'desc' : 'Key Item for Area 3'
            }
        }

    def __init__(self):
        self.items = items


class MapDefs:
    global areas
    global roomvars
    
    areas = {
        'area1' : {
                'rooms' : [ 6, 6 ],
                'loot' : [ items['terminal'], items['key1'] ],
                'itemloc' : [ 0, 3 ],
                'name' : "Area One"
        },
        'area2' : {
                'rooms' : [ 6, 6 ],
                'loot' : [ items['terminal'], items['key2'] ],
                'itemloc' : [ 0, 3 ],
                'name' : "Area Two"
        },
        'area3' : {
                'rooms' : [ 6, 6 ],
                'loot' : [ items['terminal'], items['key3'] ],
                'itemloc' : [ 0, 3 ],
                'name' : "Area Three"
        }
    }
    
    roomvars = {
        # for exitlocs, its [(north), (south), (east), (west)]
        'area1main' : {
            'soundtrack' : ['s1'],
            'background' : ['A1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'north', 'west', 'east' ],
            'exitindex' : [ 3, 5, 1]
        },
        'area1r1' : {
            'soundtrack' : ['s1'],
            'background' : [ 'A2.gif' ],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'north', 'west' ],
            'exitindex' : [ 2, 0]
        },
        'area1r2' : {
            'soundtrack' : ['s1'],
            'background' : ['A3.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'west' ],
            'exitindex' : [ 1, 3]
        },
        'area1keyroom' : {
            'soundtrack' : ['s1'],
            'background' : ['A4.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'west', 'east' ],
            'exitindex' : [ 0, 4, 2]
        },
        'area1r3' : {
            'soundtrack' : ['s1'],
            'background' : ['b1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'east'],
            'exitindex' : [ 5, 3 ]
        },
        'area1exit' : {
            'soundtrack' : ['s1'],
            'background' : ['Background.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'north', 'south', 'east' ],
            'exitindex' : [ 4, 6, 0 ]
        },
        'area2main' : {
            'soundtrack' : ['s1'],
            'background' : ['B1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'east', 'north', 'west' ],
            'exitindex' : [ 1, 3, 5]
        },
        'area2r1' : {
            'soundtrack' : ['s1'],
            'background' : [ 'B2.gif' ],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'west', 'north' ],
            'exitindex' : [ 0, 2]
        },
        'area2r2' : {
            'soundtrack' : ['s1'],
            'background' : ['B3.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'west' ],
            'exitindex' : [ 1, 3]
        },
        'area2keyroom' : {
            'soundtrack' : ['s1'],
            'background' : ['B4.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'west', 'east' ],
            'exitindex' : [ 0, 4, 2]
        },
        'area2r3' : {
            'soundtrack' : ['s1'],
            'background' : ['B5.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'east', 'south'],
            'exitindex' : [ 3, 5 ]
        },
        'area2exit' : {
            'soundtrack' : ['s1'],
            'background' : ['B6.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'north', 'east' ],
            'exitindex' : [ 4, 6 ]
        },
        'area3main' : {
            'soundtrack' : ['s1'],
            'background' : ['C1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'east', 'north', 'west' ],
            'exitindex' : [ 1, 3, 5]
        },
        'area3r1' : {
            'soundtrack' : ['s1'],
            'background' : [ 'C2.gif' ],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'west', 'north' ],
            'exitindex' : [ 0, 2]
        },
        'area3r2' : {
            'soundtrack' : ['s1'],
            'background' : ['C3.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'west' ],
            'exitindex' : [ 1, 3]
        },
        'area3keyroom' : {
            'soundtrack' : ['s1'],
            'background' : ['C4.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'west', 'east' ],
            'exitindex' : [ 0, 4, 2]
        },
        'area3r3' : {
            'soundtrack' : ['s1'],
            'background' : ['C5.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'east', 'south'],
            'exitindex' : [ 3, 5 ]
        },
        'area3exit' : {
            'soundtrack' : ['s1'],
            'background' : ['C6.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'north', 'east' ],
            'exitindex' : [ 4, 6 ]
        }
    }
    
    def __init__(self):
        self.roomvars = roomvars
        self.areas = areas

        
