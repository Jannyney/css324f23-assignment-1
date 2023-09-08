def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s #xmax = 8L, ymax = 5L, zmax = 3L
    #Fill a 5L-bottle
    t = 5 - y
    if x>0 and t>0: #Pour 8L-bottle into 5L-bottle
        if x>t:
            yield((x-t,5,z), t)
        else:
            yield((0,y+x,z), x)
    if z>0 and t>0: #Pour 3L-bottle into 8L-bottle
        if z>t:
            yield((x,5,z-t), t)
        else:
            yield((x,y+z,0), z)
    #Fill a 3L-bottle 
    t = 3 - z 
    if x>0 and t>0: #Pour 8L-bottle into 3L-bottle
        if x>t: 
            yield((x-t,y,3), t) 
        else:
            yield((0,y,z+x), x)
    if y>0 and t>0: #Pour 5L-bottle into 3L-bottle
        if y>t:
            yield((x,y-t,3), t)
        else:
            yield((x,0,z+y), y)
    #Fill a 8L-bottle
    t = 8 - x
    if y>0 and t>0: #Pour 5L-bottle into 8L-bottle
        if y>t:
            yield((8,y-t,z), t)
        else:
            yield((x+y,0,z), y)
    if z>0 and t>0: #Pour 3L-bottle into 8L-bottle
        if z>t:
            yield((8,y,z-t), t)
        else:
            yield((x+z,y,0), z)
    
