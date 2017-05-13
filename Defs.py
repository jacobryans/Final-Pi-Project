class ItemDefs:
    global items

    items = {
        'terminal' : {
            'type' : 'usable',
            'pic' : [ 'terminal.png' ],
            'key' : False,
            'desc' : 'Informational Terminal'
            },
        'key1' : {
            'type' : 'read',
            'pic' : [ 'key1.png' ],
            'key' : True,
            'desc' : 'Key Item for Area 1'
            },
        'key2' : {
            'type' : 'read',
            'pic' : [ 'key2.png' ],
            'key' : True,
            'desc' : 'Key Item for Area 2'
            },
        'key3' : {
            'type' : 'read',
            'pic' : [ 'key3.png' ],
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
                #'itemlist' : [ items['terminal'], items['key1'] ],
                'name' : "Area One"
        },
        'area2' : {
                'rooms' : [ 6, 6 ],
                #'itemlist' : [ items['terminal'], items['key2'] ],
                'name' : "Area Two"
        },
        'area3' : {
                'rooms' : [ 6, 6 ],
                #'itemlist' : [ items['terminal'], items['key3'] ],
                'name' : "Area Three"
        }
    }
    
    roomvars = {
        # for exitlocs, its [(north), (south), (east), (west)]
        'area1main' : {
            'soundtrack' : ['s1'],
            'background' : ['A1.gif'],
            'exitlocs' : [(250, 120), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'north' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 1 ]
        },
        'area1r1' : {
            'soundtrack' : ['s1'],
            'background' : [ 'A2.gif' ],
            'exitlocs' : [(250, 0), (250, 470), (20, 250), (470, 250)],
            'exits' : [ 'north' ,'east', 'south', 'west' ],
            'itemlist' : [ items['terminal'] ],
            'itempos' : [ 350, 250 ],
            'exitindex' : [ 3, 2, 0, 5]
        },
        'area1r2' : {
            'soundtrack' : ['s1'],
            'background' : ['A3.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'west' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 1 ]
        },
        'area1keyroom' : {
            'soundtrack' : ['s1'],
            'background' : ['A4.gif'],
            'exitlocs' : [(250, 0), (250, 470), (20, 250), (500, 250)],
            'exits' : [ 'west', 'south'],
            'itemlist' : [ items['key1'] ],
            'itempos' : [ 240, 60 ],
            'exitindex' : [ 4, 1 ]
        },
        'area1r3' : {
            'soundtrack' : ['s1'],
            'background' : ['A5.gif'],
            'exitlocs' : [(250, 0), (250, 450), (0, 250), (450, 250)],
            'exits' : [ 'south', 'east'],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 5, 3]
        },
        'area1exit' : {
            'soundtrack' : ['s1'],
            'background' : ['A6.gif'],
            'exitlocs' : [(250, 30), (250, 450), (0, 250), (470, 300)],
            'exits' : [ 'north', 'east', 'south' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 4, 1, 6 ]
        },
        'area2main' : {
            'soundtrack' : ['s1'],
            'background' : ['B1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'north', 'west', 'east' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 1, 3, 5]
        },
        'area2r1' : {
            'soundtrack' : ['s1'],
            'background' : [ 'B2.gif' ],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'west', 'north' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 0, 2]
        },
        'area2r2' : {
            'soundtrack' : ['s1'],
            'background' : ['B3.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'west' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 1, 3]
        },
        'area2keyroom' : {
            'soundtrack' : ['s1'],
            'background' : ['B4.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'west', 'east' ],
            'itemlist' : [ items['key2'] ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 0, 4, 2]
        },
        'area2r3' : {
            'soundtrack' : ['s1'],
            'background' : ['B5.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'east', 'south'],
            'itemlist' : [ items['terminal'] ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 3, 5 ]
        },
        'area2exit' : {
            'soundtrack' : ['s1'],
            'background' : ['B6.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'north', 'south' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 4, 6 ]
        },
        'area3main' : {
            'soundtrack' : ['s1'],
            'background' : ['C1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'east', 'north', 'west' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 1, 3, 5]
        },
        'area3r1' : {
            'soundtrack' : ['s1'],
            'background' : [ 'C2.gif' ],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'west', 'north' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 0, 2]
        },
        'area3r2' : {
            'soundtrack' : ['s1'],
            'background' : ['C3.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'west' ],
            'itemlist' : [ items['terminal'] ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 1, 3]
        },
        'area3keyroom' : {
            'soundtrack' : ['s1'],
            'background' : ['C4.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'west', 'east' ],
            'itemlist' : [ items['key3'] ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 0, 4, 2]
        },
        'area3r3' : {
            'soundtrack' : ['s1'],
            'background' : ['C5.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'east', 'south'],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 3, 5 ]
        },
        'area3exit' : {
            'soundtrack' : ['s1'],
            'background' : ['C6.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'north', 'south' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 4, 6 ]
        }
    }
    
    def __init__(self):
        self.roomvars = roomvars
        self.areas = areas

        
