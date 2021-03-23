### 2D rubiks cube simulation ##

# Each "side" of the cube will be represented my a matrix. Wish me luck

import numpy as np
import show, movement

### SIDE IDENTIFIERS ###
# Front -> 0
# Back -> 1
# Up -> 2
# Down -> 3
# Left -> 4
# Right -> 5


# Cube init
Cube = {}
i = 0
for letter in 'FBUDLR':
    Cube[letter] = i * np.ones((2,2))
    i = i+1

show.print_cube(Cube)
movement.move(Cube, 'F', True)
show.print_cube(Cube)
