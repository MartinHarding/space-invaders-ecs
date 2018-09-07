"""Vectors module tests"""

from space_invaders.vectors import Vector2

def test_vector2():
    """Test Vector2 class"""
    x = 0
    y = 0
    vector2 = Vector2(x, y)
    assert vector2.x == x
    assert vector2.y == y
