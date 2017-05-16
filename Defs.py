class ItemDefs:
    global items

    items = {
        'terminal' : {
            'type' : 'usable',
            'pic' : [ 'pic/terminal.png' ],
            'key' : False,
            'desc' : 'Informational Terminal'
            },
        'key1' : {
            'type' : 'read',
            'pic' : [ 'pic/key1.png' ],
            'key' : True,
            'desc' : 'Key Item for Area 1'
            },
        'key2' : {
            'type' : 'read',
            'pic' : [ 'pic/key2.png' ],
            'key' : True,
            'desc' : 'Key Item for Area 2'
            },
        'key3' : {
            'type' : 'read',
            'pic' : [ 'pic/key3.png' ],
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
            'background' : ['pic/A1.gif'],
            'exitlocs' : [(250, 120), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'north' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 1 ]
        },
        'area1r1' : {
            'soundtrack' : ['s1'],
            'background' : [ 'pic/A2.gif' ],
            'exitlocs' : [(250, 0), (250, 470), (20, 250), (470, 250)],
            'exits' : [ 'north' ,'east', 'south', 'west' ],
            'itemlist' : [ items['terminal'] ],
            'itempos' : [ 350, 250 ],
            'exitindex' : [ 3, 2, 0, 5]
        },
        'area1r2' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/A3.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'west' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 1 ]
        },
        'area1keyroom' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/A4.gif'],
            'exitlocs' : [(250, 0), (250, 470), (20, 250), (500, 250)],
            'exits' : [ 'west', 'south'],
            'itemlist' : [ items['key1'] ],
            'itempos' : [ 240, 60 ],
            'exitindex' : [ 4, 1 ]
        },
        'area1r3' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/A5.gif'],
            'exitlocs' : [(250, 0), (250, 450), (0, 250), (450, 250)],
            'exits' : [ 'south', 'east'],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 5, 3]
        },
        'area1exit' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/A6.gif'],
            'exitlocs' : [(250, 30), (250, 450), (0, 250), (470, 300)],
            'exits' : [ 'south', 'east', 'north' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 6, 1, 4 ]
        },
        'area2main' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/B1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (40, 250), (460, 250)],
            'exits' : [ 'east', 'west' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 1, 5 ]
        },
        'area2r1' : {
            'soundtrack' : ['s1'],
            'background' : [ 'pic/B2.gif' ],
            'exitlocs' : [(250, 0), (250, 470), (40, 250), (460, 250)],
            'exits' : [ 'west', 'east' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 0, 2 ]
        },
        'area2r2' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/B3.gif'],
            'exitlocs' : [(250, 0), (250, 500), (40, 250), (460, 250)],
            'exits' : [ 'west', 'east' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 1, 3]
        },
        'area2keyroom' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/B4.gif'],
            'exitlocs' : [(250, 40), (250, 500), (0, 250), (460, 250)],
            'exits' : [ 'north', 'west' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 4, 2]
        },
        'area2r3' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/B5.gif'],
            'exitlocs' : [(250, 0), (250, 470), (0, 250), (500, 250)],
            'exits' : [ 'south' ],
            'itemlist' : [ items['key2'] ],
            'itempos' : [ 250, 100 ],
            'exitindex' : [ 3 ]
        },
        'area2exit' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/B6.gif'],
            'exitlocs' : [(250, 0), (250, 470), (0, 250), (460, 250)],
            'exits' : [ 'south', 'east' ],
            'itemlist' : [ items['terminal'] ],
            'itempos' : [ 100, 300 ],
            'exitindex' : [ 6, 1 ]
        },
        'area3main' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/C1.gif'],
            'exitlocs' : [(250, 0), (250, 500), (30, 250), (500, 250)],
            'exits' : [ 'west' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 1 ]
        },
        'area3r1' : {
            'soundtrack' : ['s1'],
            'background' : [ 'pic/C2.gif' ],
            'exitlocs' : [(250, 30), (250, 470), (0, 250), (470, 250)],
            'exits' : [ 'east', 'north', 'south' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 0, 2, 4 ]
        },
        'area3r2' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/C3.gif'],
            'exitlocs' : [(250, 30), (250, 470), (30, 250), (500, 250)],
            'exits' : [ 'south', 'north' ],
            'itemlist' : [ items['terminal'] ],
            'itempos' : [ 400, 200 ],
            'exitindex' : [ 1, 3]
        },
        'area3keyroom' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/C4.gif'],
            'exitlocs' : [(250, 0), (250, 470), (0, 250), (500, 250)],
            'exits' : [ 'south' ],
            'itemlist' : [ items['key3'] ],
            'itempos' : [ 250, 150 ],
            'exitindex' : [ 2 ]
        },
        'area3r3' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/C5.gif'],
            'exitlocs' : [(250, 40), (250, 470), (0, 250), (500, 250)],
            'exits' : [ 'north', 'south'],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 1, 5 ]
        },
        'area3exit' : {
            'soundtrack' : ['s1'],
            'background' : ['pic/C6.gif'],
            'exitlocs' : [(250, 0), (250, 500), (0, 250), (500, 250)],
            'exits' : [ 'south', 'north' ],
            'itemlist' : [ ],
            'itempos' : [ 300, 0 ],
            'exitindex' : [ 6, 4 ]
        }
    }
    
    def __init__(self):
        self.roomvars = roomvars
        self.areas = areas

        
