"""Entities module tests"""
import pytest

from space_invaders.entities import Entity
from space_invaders.components import Component

def test_entity():
    """Test initializing an entity."""
    entity = Entity()
    assert entity.uid

def test_add_component():
    """Test adding a componenting to an entity."""
    entity = Entity()
    component = Component()
    entity.add_component(component)
    assert entity.components[0] == component


def test_add_component_duplicate():
    """Test adding a componenting to an entity."""
    entity = Entity()
    entity.add_component(Component())
    with pytest.raises(AssertionError):
        entity.add_component(Component())


def test_remove_component():
    """Test removing a component from an entity."""
    entity = Entity()
    component = Component()
    entity.add_component(component)
    entity.remove_component(Component)
    assert not entity.components

def test_get_component():
    """Test getting a component attached to an entity."""

    class Component1(Component):
        """Dummy class for testing"""
        pass

    class Component2(Component):
        """Dummy class for testing"""
        pass

    entity = Entity()
    component1 = Component1()
    component2 = Component2()
    entity.add_component(component1)
    entity.add_component(component2)
    assert entity.get_component(Component1) == component1
    assert entity.get_component(Component2) == component2
