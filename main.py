# My modules
import transformations as tf
import drawing as draw

def prompt_user():
    """
    Prompts the user for input.
    """

    prompt = '\nWould you like to draw a cube or a triangular prism?\n'
    prompt += 'Enter 1 for cube, or enter 2 for triangular prism: '
    answer = int(input(prompt))

    while answer != 1 and answer != 2:
        if answer == 1:
            draw.draw_cube()
            prompt_transformations("cube")
        elif answer == 2:
            draw.draw_tri_prism()
            prompt_transformations("prism")
        else:
            print("Invalid input, try again.")


def prompt_transformations(shape):
    """
    Prompts the user to apply transformations to the shape.
    """
    prompt = "Choose to apply a transformation:\n1: Translation\n2: Rotation\n3: Scale\n4: Quit\n"
    cmd = 0
    while cmd != 4:
        cmd = int(input(prompt))

        # Cube transformations
        if shape == "cube":

            # Translation
            if cmd == 1:
                Tx = float(input("Enter x-displacement: "))
                Ty = float(input("Enter y-displacement: "))
                Tz = float(input("Enter z-displacement: "))
                draw.draw_new_cube(tf.translate(Tx, Ty, Tz))

            # Rotation
            elif cmd == 2:
                angle = float(input("Enter the angle you wish to rotate the shape: "))
                axis = input("Enter which axis you wish to perform the rotation about (x, y, z): ")
                if axis == "x":
                    draw.draw_new_cube(tf.rotate_x(angle))
                elif axis == "y":
                    draw.draw_new_cube(tf.rotate_y(angle))
                elif axis == "z":
                    draw.draw_new_cube(tf.rotate_z(angle))
                else:
                    print("Invalid input, try again")
                
            # Scale
            elif cmd == 3:
                Sx = float(input("Enter x scaling factor: "))
                Sy = float(input("Enter y scaling factor: "))
                Sz = float(input("Enter z scaling factor: "))
                Cx = float(input("Enter x-coord for center of scale: "))
                Cy = float(input("Enter y-coord for center of scale: "))
                Cz = float(input("Enter z-coord for center of scale: "))
                draw.draw_new_cube(tf.scale(Sx, Sy, Sz, Cx, Cy, Cz))
        
        # Triangular Prism transformations
        else:

            # Translation
            if cmd == 1:
                Tx = float(input("Enter x-displacement: "))
                Ty = float(input("Enter y-displacement: "))
                Tz = float(input("Enter z-displacement: "))
                draw.draw_new_prism(tf.translate(Tx, Ty, Tz))

            # Rotation
            elif cmd == 2:
                angle = float(input("Enter the angle you wish to rotate the shape: "))
                axis = input("Enter which axis you wish to perform the rotation about (x, y, z): ")
                if axis == "x":
                    draw.draw_new_prism(tf.rotate_x(angle))
                elif axis == "y":
                    draw.draw_new_prism(tf.rotate_y(angle))
                elif axis == "z":
                    draw.draw_new_prism(tf.rotate_z(angle))
                else:
                    print("Invalid input, try again")
                
            # Scale
            elif cmd == 3:
                Sx = float(input("Enter x scaling factor: "))
                Sy = float(input("Enter y scaling factor: "))
                Sz = float(input("Enter z scaling factor: "))
                Cx = float(input("Enter x-coord for center of scale: "))
                Cy = float(input("Enter y-coord for center of scale: "))
                Cz = float(input("Enter z-coord for center of scale: "))
                draw.draw_new_prism(tf.scale(Sx, Sy, Sz, Cx, Cy, Cz))


if __name__ == '__main__':
    prompt_user()