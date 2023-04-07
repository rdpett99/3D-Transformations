"""
This program implements a basic line scan-conversion (line drawing)
algorithm. This program uses the Python Imaging Library in order to
assist with line drawing.
"""

# Standard Libraries
import math

# Image module from the Python Imaging Library
from PIL import Image

# Creates an empty black image
image = Image.new(mode = "RGB", size = (500, 500), color = (0,0,0))


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
                image.putpixel((x, y), (r, g, b))

        # Check if |x1 - x0| < |y1 - y0|
        elif (abs(x1 - x0) < abs(y1 - y0)):
            y_min = min(y0, y1)

            # Critical loop
            for y_coord in range(abs(y1 - y0) + 1):
                y = y_min + y_coord
                x = (y - y_intercept) / slope
                x = math.trunc(x)
                image.putpixel((x, y), (r, g, b))
    

def reset_image():
    """
    Resets the current image.
    """
    for x in range(500):
        for y in range(500):
            image.putpixel((x, y), (0, 0, 0))