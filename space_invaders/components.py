"""Component classes"""
from space_invaders.vectors import Vector2


class Component():
    """
    A component gets attached to entities and is used for storing data related
    to that entity. By themselves, entities don't do anything.
    """


class Player(Component):
    """Something which is controlled by the player"""


class Invader(Component):
    """Something which is invading"""


class Transform(Component):
    """Stores position and provides translation functionality."""

    def __init__(self, position=None):
        """
        Args:
            position (Vector2): x and y coordinates of this transform
        """
        self.position = position

    def translate(self, vector):
        """
        Moves the transforms position towards a vector.

        Args:
            vector (Vector2): [description]
        """
        assert isinstance(vector, Vector2)
        self.position.x += vector.x
        self.position.y += vector.y


class Rigidbody(Component):
    """Stores information for calculating simple rigidbody physics."""

    def __init__(self, mass, drag, velocity):
        """
        Args:
            mass (float): relative mass of the simulated object.
            velocity (Vector2): current velocity of the simulated object.
            drag (float): drag to be applied to the simulated object.
        """
        self.mass = mass
        self.drag = drag
        self.velocity = velocity


class Box(Component):
    """Stores the width and height representing a box."""

    def __init__(self, width, height):
        self.width = width
        self.height = height


class Fill(Component):
    """Stores color to be used for filling shapes."""

    def __init__(self, color):
        assert 0 < color < 16
        self.color = color


class Outline(Component):
    """Stores color to be used for outlining shapes."""

    def __init__(self, color):
        assert 0 < color < 16
        self.color = color
