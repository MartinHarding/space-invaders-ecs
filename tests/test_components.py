"""Components module tests"""

from space_invaders.vectors import Vector2
from space_invaders.components import Transform, Rigidbody, Box, Color

def test_transform():
    """Test initializing a transform component"""
    position = Vector2(0, 0)
    transform = Transform(position=position)
    assert transform.position == position


def test_transform_translate():
    """Test translating a transform component"""
    position = Vector2(0, 0)
    transform = Transform(position=position)

    # Move down,right by one unit
    transform.translate(Vector2(1, 1))
    expected = Vector2(1, 1)
    assert transform.position.x == expected.x
    assert transform.position.y == expected.y

    # Move up,left by two units
    transform.translate(Vector2(-2, -2))
    expected = Vector2(-1, -1)
    assert transform.position.x == expected.x
    assert transform.position.y == expected.y


def test_rigidbody():
    """Test initializing a rigidbody component"""
    mass = 1.0
    drag = 1.0
    velocity = Vector2(1, 1)
    rigidbody = Rigidbody(mass=mass, drag=drag, velocity=velocity)
    assert rigidbody.mass == mass


def test_box():
    """Test initializing a box component"""
    width = 10
    height = 10
    box = Box(width, height)
    assert box.width == width
    assert box.height == height


def test_color():
    """Test initializing a color component"""
    color_index = 1
    color = Color(color=color_index)
    assert color.color == color_index
