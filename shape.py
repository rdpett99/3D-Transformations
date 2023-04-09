class Shape:
    """
    Defines a 3D shape. In this case, either a cube or a triangular prism.
    """

    def __init__(self, shape_type: str):
        """
        Initializes the shape's attributes.
        """
        self.type = shape_type
        self.vertices = []


    def set_vertices(self):
        """
        Sets the default vertices depending on the shape type.
        """
        if self.type == 'cube':
            self.vertices = [()]