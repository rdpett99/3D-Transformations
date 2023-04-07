import math

# Scientific computing library for Python
# Used for matrix multiplication operator @
import numpy as np

"""
This program contains functions that can perform 2D line
transformations. Calculations are used by multiplying matrices.
"""

def translate(Tx, Ty, Tz):
    """
    Returns a translation matrix, where:
        Tx : displacement in the x-direction
        Ty : displacement in the y-direction
        Tz : displacement in the z-direction
    """
    return np.array([[1,  0,  0,  0],
                     [0,  1,  0,  0],
                     [0,  0,  1,  0],
                     [Tx, Ty, Tz, 1]])

def scale(Sx, Sy, Sz, Cx, Cy, Cz):
    """
    Returns a scale matrix, where:
        Sx : scale in the x-direction
        Sy : scale in the y-direction
        Sz : scale in the z-direction
        Cx : x-coordinate of center of scale
        Cy : y-coordinate of center of scale
        Cz : z-coordinate of center of scale
    
    Returned matrix is the product of three matrices:
    (1) a translation matrix moving toward the
    origin (Cx, Cy, Cz), (2) a scale matrix, and (3) 
    another translation matrix moving object back to its
    original coordinates.

             (1)                  (2)                (3)

    [1,    0,   0,  0]     [Sx, 0,  0,  0]     [1,  0,  0,  0]
    [0,    1,   0,  0]  X  [0,  Sy, 0,  0]  X  [0,  1,  0,  0]
    [0,    0,   1,  0]     [0,  0,  Sz, 0]     [0,  0,  1,  0]
    [-Cx, -Cy, -Cz, 1]     [0,  0,  0,  1]     [Cx, Cy, Cz, 1]

    """
    t1_matrix = translate(-Cx, -Cy, -Cz)
    s_matrix = np.array([[Sx, 0,  0,  0],
                         [0,  Sy, 0,  0],
                         [0,  0,  Sz, 0],
                         [0,  0,  0,  1]])
    t2_matrix = translate(Cx, Cy, Cz)

    return t1_matrix @ s_matrix @ t2_matrix