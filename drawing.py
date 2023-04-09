"""
This program implements a basic line scan-conversion (line drawing)
algorithm. This program uses the Python Imaging Library in order to
assist with line drawing.
"""

# Standard Libraries
import math

# Image module from the Python Imaging Library
from PIL import Image

# Scientific computing library for Python
# Used for matrix multiplication operator @
import numpy as np

import transformations as tf

# Creates an empty black image
image = Image.new(mode = "RGB", size = (1024, 1024), color = (0,0,0))


def draw_line(x0, y0, x1, y1):
    """
    This function draws a line starting at point (x0, y0) and ending at point 
    (x1, y1) in a standard coordinate system. 
    """

    # RGB values
    r, g, b = 255, 255, 255

    # If x0 == x1 : the line is vertical
    if x0 == x1:
        y_min = min(y0, y1)

        # Critical loop
        for y_coord in range(abs(y1 - y0)):
            if (x0 > -1 and x0 < 1024) and (y_min + y_coord > -1 and y_min + y_coord < 1024):
                image.putpixel((x0, y_min + y_coord), (r, g, b))
    
    # Else, the line is not vertical
    else:

        # Calculates the slope and y-intercept
        slope = (y1 - y0) / (x1 - x0)
        y_intercept = y1 - (slope * x1)

        # Check if |x1 - x0| >= |y1 - y0|
        if (abs(x1 - x0) >= abs(y1 - y0)):
            x_min = min(x0, x1)

            # Critical loop
            for x_coord in range(abs(x1 - x0) + 1):
                x = x_min + x_coord
                y = (slope * x) + y_intercept
                y = math.trunc(y)
                if (x > -1 and x < 1024) and (y > -1 and y < 1024):
                    image.putpixel((x, y), (r, g, b))

        # Check if |x1 - x0| < |y1 - y0|
        elif (abs(x1 - x0) < abs(y1 - y0)):
            y_min = min(y0, y1)

            # Critical loop
            for y_coord in range(abs(y1 - y0) + 1):
                y = y_min + y_coord
                x = (y - y_intercept) / slope
                x = math.trunc(x)
                if (x > -1 and x < 1024) and (y > -1 and y < 1024):
                    image.putpixel((x, y), (r, g, b))
    

def draw_cube():
    cube_vertices = {
        'A': (-1,  1, -1),
        'B': ( 1,  1, -1),
        'C': ( 1, -1, -1),
        'D': (-1, -1, -1),
        'E': (-1,  1,  1),
        'F': ( 1,  1,  1),
        'G': ( 1, -1,  1),
        'H': (-1, -1,  1)
    }

    # Transform all cube vertices from the WCS to the ECS
    eyeCS_tf_matrix = tf.eyeCS_conversion(6, 8, 7.5, 60, 15)
    for vertex_key, vertex in cube_vertices.items():
        matrix = np.array(vertex) @ eyeCS_tf_matrix
        cube_vertices[vertex_key] = matrix
    
    # Perspective projection
    cube_2Dcoords = {vertex: (0,0) for vertex in cube_vertices.keys()}
    for vertex_key, vertex in cube_vertices.items():
        x = vertex[0] / vertex[2] * 511.5 + 511.5
        y = vertex[1] / vertex[2] * 511.5 + 511.5
        cube_2Dcoords[vertex_key] = (math.trunc(x), math.trunc(y))
    
    print(cube_2Dcoords)


def reset_image():
    """
    Resets the current image.
    """
    for x in range(500):
        for y in range(500):
            image.putpixel((x, y), (0, 0, 0))