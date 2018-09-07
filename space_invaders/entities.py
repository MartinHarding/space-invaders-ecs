"""Entity classes"""

import secrets
from space_invaders.components import Component


def get_entities_by_component(entities, component_subclass):
    """
    Find all entities with a certain component.

    Args:
        entities (list): entities to filter through
        component_subclass (class): component sublcass to filter by.

    Returns:
        list, none: entities which contain a given component
    """
    found = []
    for entity in entities.values():
        for component in entity.components:
            if isinstance(component, component_subclass):
                found.append(entity)
                break
    return found


class Entity():
    """
    An entity is something that exists in the game world, and is essentially a
    list of components tagged with a unique ID.
    """

    def __init__(self):
        self.uid = secrets.token_hex(16)
        self.components = []

    def get_component(self, component_subclass):
        """
        Gets the component which is an instance of the passed in subclass.

        Args:
            component_subclass (class): component sublcass to get.

        Returns:
            object, none: component which matches the passed in class
        """
        assert issubclass(component_subclass, Component)
        for component in self.components:
            if isinstance(component, component_subclass):
                return component
        return None

    def remove_component(self, component_subclass):
        """
        Removes the component which is an instance of the passed in class.

        Args:
            component_subclass (class): component sublcass to remove.
        """
        for component in self.components:
            if isinstance(component, component_subclass):
                self.components.remove(component)

    def add_component(self, component):
        """
        Adds a component to an entity.

        Args:
            component (object): component to add
        """
        assert issubclass(type(component), Component)
        assert self.get_component(type(component)) is None
        self.components.append(component)
