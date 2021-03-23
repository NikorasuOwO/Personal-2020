import numpy as np

def movement(Cube, side, conventional):
    if Cube[side]%2 != 0: # We find the opposite side of the one we will make the movement
        opposite_side = Cube[Cube[side]-1]
    else: opposite_side = Cube[Cube[side]+1]

    for side in Cube.keys().remove(opposite_side):
        
