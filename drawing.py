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

# Pandas library for csv
import csv

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
    """
    Reads from the cube_table.csv file and applies both the conversion
    from the World Coordinate System to the Eye Coordinate System on each 
    vertex, as well as Perspective Projection of a 3D shape on a 2D screen.
    After, it draws the resultant cube.
    """

    # Holds the values from cube_table.csv
    cube_coordinates = {}

    # Read coordinates from "cube_table.csv" and assign them to the dictionary coordinates
    with open("cube_table.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        i = 0
        for line in csvreader:
            temp = []
            for num in line:
                temp.append(int(num))
            cube_coordinates[int(i)] = temp
            i += 1
    
    # Applies WCS -> ECS conversion and Perspective Projection
    cube_vertex_table = {}
    for i, val in cube_coordinates.items():

        # WCS -> ECS
        eye_matrix = tf.eyeCS_conversion(6,8,7.5,60,15)
        cube_coordinates[i] = np.array(val) @ eye_matrix

        # Perspective Projection
        x = (cube_coordinates[i][0] / cube_coordinates[i][2]) * 511.5 + 511.5
        y = (cube_coordinates[i][1] / cube_coordinates[i][2]) * 511.5 + 511.5
        cube_vertex_table[i] = [math.trunc(x), math.trunc(y)]
    
    # Draws the cube
    draw_line(
        cube_vertex_table[0][0], cube_vertex_table[0][1],
        cube_vertex_table[1][0], cube_vertex_table[1][1]
    )
    draw_line(
        cube_vertex_table[1][0], cube_vertex_table[1][1],
        cube_vertex_table[2][0], cube_vertex_table[2][1]
    )
    draw_line(
        cube_vertex_table[2][0], cube_vertex_table[2][1],
        cube_vertex_table[3][0], cube_vertex_table[3][1]
    )
    draw_line(
        cube_vertex_table[3][0], cube_vertex_table[3][1],
        cube_vertex_table[0][0], cube_vertex_table[0][1]
    )

    draw_line(
        cube_vertex_table[4][0], cube_vertex_table[4][1],
        cube_vertex_table[5][0], cube_vertex_table[5][1]
    )
    draw_line(
        cube_vertex_table[5][0], cube_vertex_table[5][1],
        cube_vertex_table[6][0], cube_vertex_table[6][1]
    )
    draw_line(
        cube_vertex_table[6][0], cube_vertex_table[6][1],
        cube_vertex_table[7][0], cube_vertex_table[7][1]
    )
    draw_line(
        cube_vertex_table[7][0], cube_vertex_table[7][1],
        cube_vertex_table[4][0], cube_vertex_table[4][1]
    )

    draw_line(
        cube_vertex_table[0][0], cube_vertex_table[0][1],
        cube_vertex_table[4][0], cube_vertex_table[4][1]
    )
    draw_line(
        cube_vertex_table[1][0], cube_vertex_table[1][1],
        cube_vertex_table[5][0], cube_vertex_table[5][1]
    )
    draw_line(
        cube_vertex_table[2][0], cube_vertex_table[2][1],
        cube_vertex_table[6][0], cube_vertex_table[6][1]
    )
    draw_line(
        cube_vertex_table[3][0], cube_vertex_table[3][1],
        cube_vertex_table[7][0], cube_vertex_table[7][1]
    )
    image.show()


def draw_tri_prism():
    """
    Reads from the tri_prism_table.csv file and applies both the conversion
    from the World Coordinate System to the Eye Coordinate System on each 
    vertex, as well as Perspective Projection of a 3D shape on a 2D screen.
    After, it draws the resultant triangular prism.
    """

    # Holds the values from tri_prism_table.csv
    tri_prism_coordinates = {}

    # Read coordinates from "tri_prism_table.csv" and assign them to the dictionary coordinates
    with open("tri_prism_table.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        i = 0
        for line in csvreader:
            temp = []
            for num in line:
                temp.append(int(num))
            tri_prism_coordinates[int(i)] = temp
            i += 1 
    
    # Applies WCS -> ECS conversion and Perspective Projection
    prism_vertex_table = {}
    for i, val in tri_prism_coordinates.items():

        # WCS -> ECS
        eye_matrix = tf.eyeCS_conversion(6,8,7.5,60,15)
        tri_prism_coordinates[i] = np.array(val) @ eye_matrix

        # Perspective Projection
        x = (tri_prism_coordinates[i][0] / tri_prism_coordinates[i][2]) * 511.5 + 511.5
        y = (tri_prism_coordinates[i][1] / tri_prism_coordinates[i][2]) * 511.5 + 511.5
        prism_vertex_table[i] = [math.trunc(x), math.trunc(y)]
    
    # Draws the triangular prism
    draw_line(
        prism_vertex_table[0][0], prism_vertex_table[0][1],
        prism_vertex_table[1][0], prism_vertex_table[1][1]
    )
    draw_line(
        prism_vertex_table[1][0], prism_vertex_table[1][1],
        prism_vertex_table[2][0], prism_vertex_table[2][1]
    )
    draw_line(
        prism_vertex_table[2][0], prism_vertex_table[2][1],
        prism_vertex_table[3][0], prism_vertex_table[3][1]
    )
    draw_line(
        prism_vertex_table[3][0], prism_vertex_table[3][1],
        prism_vertex_table[0][0], prism_vertex_table[0][1]
    )
    draw_line(
        prism_vertex_table[0][0], prism_vertex_table[0][1],
        prism_vertex_table[4][0], prism_vertex_table[4][1]
    )
    draw_line(
        prism_vertex_table[1][0], prism_vertex_table[1][1],
        prism_vertex_table[5][0], prism_vertex_table[5][1]
    )
    draw_line(
        prism_vertex_table[4][0], prism_vertex_table[4][1],
        prism_vertex_table[5][0], prism_vertex_table[5][1]
    )
    draw_line(
        prism_vertex_table[2][0], prism_vertex_table[2][1],
        prism_vertex_table[5][0], prism_vertex_table[5][1]
    )
    draw_line(
        prism_vertex_table[3][0], prism_vertex_table[3][1],
        prism_vertex_table[4][0], prism_vertex_table[4][1]
    )
    image.show()


def reset_image():
    """
    Resets the current image.
    """
    for x in range(1024):
        for y in range(1024):
            image.putpixel((x, y), (0, 0, 0))