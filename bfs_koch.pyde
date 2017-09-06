from koch import BFS_koch, s32

def setup():
    global k
    size(800, 800)
    background(0)
    noStroke()
    noSmooth()
    k = BFS_koch(600, 100, 600)
    fill(255)
    triangle(100, 600,
             700, 600,
             400, 600 - 600 * s32)

def draw():
    next(k)