from math import sin, cos, radians, sqrt

# Scientific computing library for Python
# Used for matrix multiplication operator @
import numpy as np

"""
This program contains functions that can perform 3D line
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


def rotate_x(angle):
    """
    Returns a rotation matrix that'll perform a rotation
    about the x-axis, where:
        angle : degrees in radians
    """
    theta = radians(angle)
    sin0  = sin(theta)
    cos0  = cos(theta)

    return np.array([[1,   0,     0,   0],
                     [0,  cos0,  sin0, 0],
                     [0, -sin0,  cos0, 0],
                     [0,   0,     0,   0]])


def rotate_y(angle):
    """
    Returns a rotation matrix that'll perform a rotation
    about the y-axis, where:
        angle : degrees in radians
    """
    theta = radians(angle)
    sin0  = sin(theta)
    cos0  = cos(theta)

    return np.array([[cos0, 0, -sin0,  0],
                     [0,    1,   0,    0],
                     [sin0, 0,  cos0,  0],
                     [0,    0,   0,    1]])


def rotate_z(angle):
    """
    Returns a rotation matrix that'll perform a rotation
    about the z-axis, where:
        angle : degrees in radians
    """
    theta = radians(angle)
    sin0  = sin(theta)
    cos0  = cos(theta)

    return np.array([[cos0,  sin0, 0, 0],
                     [-sin0, cos0, 0, 0],
                     [0,      0,   1, 0],
                     [0,      0,   0, 1]])


def eyeCS_conversion(Xw, Yw, Zw, D, S):
    """
    Returns a transformation matrix that converts an image
    from the World Coordinate System (WCS) to the Eye Coordinate
    System (ECS), where:
        Xw : x-coordinate in the WCS
        Yw : y-coordinate in the WCS
        Zw : z-coordinate in the WCS
        D  : distance from the screen
        S  : 1/2 height of the screen
    """
    t_matrix = translate(-Xw, -Yw, -Zw)

    const_matrix = np.array([[1, 0,  0, 0],
                             [0, 0, -1, 0],
                             [0, 1,  0, 0],
                             [0, 0,  0, 1]])

    # magnitudes used for ry_matrix
    ry_mag1 = Yw/sqrt(Xw**2 + Yw**2)
    ry_mag2 = Xw/sqrt(Xw**2 + Yw**2)

    ry_matrix = np.array([[-ry_mag1, 0,  ry_mag2, 0],
                          [    0,    1,     0,    0],
                          [-ry_mag2, 0, -ry_mag1, 0],
                          [    0,    0,     0,    1]])

    # magnitudes used for rx_matrix
    rx_mag1 = sqrt(Xw**2 + Yw**2)/sqrt(Zw**2 + (sqrt(Xw**2 + Yw**2)**2))
    rx_mag2 = Zw/sqrt(Zw**2 + (sqrt(Xw**2 + Yw**2)**2))

    rx_matrix = np.array([[1,     0,       0,    0],
                          [0,  rx_mag1, rx_mag2, 0],
                          [0, -rx_mag2, rx_mag1, 0],
                          [0,     0,       0,    1]])

    rz_matrix = np.array([[1, 0,  0, 0],
                          [0, 1,  0, 0],
                          [0, 0, -1, 0],
                          [0, 0,  0, 1]])

    N_matrix = np.array([[D/S,  0,  0, 0],
                         [0,   D/S, 0, 0],
                         [0,    0,  1, 0],
                         [0,    0,  0, 1]])

    return t_matrix @ const_matrix @ ry_matrix @ rx_matrix @ rz_matrix @ N_matrix