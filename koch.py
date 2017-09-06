import itertools

s3 = sqrt(3)
s32 = sqrt(3) / 2
s34 = sqrt(3) / 4
ttpi = THIRD_PI * 0.5

ks_3_th = atan(sqrt(3) / 3)

def _BFS_koch(base, trig_t, x, y, rot, pilot):
    pushMatrix()
    translate(x, y)
    rotate(rot * THIRD_PI)
    triangle(base[1], 0,
             base[2], 0,
             base[4], base[3])
    popMatrix()
    
    children = [_BFS_koch(base, trig_t, x, y, rot, pilot),
                _BFS_koch(base, trig_t, x + base[1] * trig_t[rot % 6 + 6], y + base[1] * trig_t[rot % 6], rot + 1,  False),
                _BFS_koch(base, trig_t, x + base[5] * trig_t[rot % 6 + 18], y + base[5] * trig_t[rot % 6 + 12], rot - 1, False),
                _BFS_koch(base, trig_t, x + base[2] * trig_t[rot % 6 + 6], y + base[2] * trig_t[rot % 6], rot, False),
                ]

    yield
    
    if pilot:
        base[:] = [i / 3.0 for i in base]

    for i in itertools.cycle(children):
        yield next(i)
        
def BFS_koch(base, x, y):
    base_ar = [base, #0
               base / 3.0, #1
               2 * base / 3.0, #2
               base * s32 / 3.0, #3
               base * 0.5, #4
               base * sqrt(3) / 3.0, #5
              ]

    trig_t = ([sin(THIRD_PI * i) for i in range(6)] +
              [cos(THIRD_PI * i) for i in range(6)] +
              [sin(THIRD_PI * i + ks_3_th) for i in range(6)] +
              [cos(THIRD_PI * i + ks_3_th) for i in range(6)])

    for i in  itertools.cycle([_BFS_koch(base_ar, trig_t, x, y, 0, True),
                               _BFS_koch(base_ar, trig_t, x + base, y, 4, False),
                               _BFS_koch(base_ar, trig_t, x + base * 0.5, y - base * s32, 2, False),
                               ]):
        yield next(i)