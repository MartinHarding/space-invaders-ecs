"""System classes"""
import pyxel

from space_invaders.components import (Box, Fill, Invader, Outline, Player,
                                       Transform)
from space_invaders.entities import get_entities_by_component
from space_invaders.vectors import Vector2


class System():
    """
    Systems operate on the components of entities. This is where all the game
    logic happens.
    """

    def __init__(self, app):
        self.app = app

    def update(self):
        """Default method called on updating each frame"""
        pass

    def draw(self):
        """Default method called on drawing screen"""
        pass


class Input(System):
    """Input and control system"""

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # Don't process non-menu keys
        if not self.app.playing:
            return
        if pyxel.btn(pyxel.KEY_LEFT):
            self.move_player(Vector2(-1, 0))
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.move_player(Vector2(1, 0))

    def move_player(self, vector):
        """Moves the player"""
        players = get_entities_by_component(self.app.entities, Player)
        for player in players:
            transform = player.get_component(Transform)
            box = player.get_component(Box)

            # Trying to move left, but already against wall, so return
            left_edge = transform.position.x
            if vector.x < 0 and left_edge <= 0:
                return

            # Trying to move right, but already against wall, so return
            right_edge = transform.position.x + box.width
            if vector.x > 0 and right_edge >= self.app.width - 1:
                return

            transform.translate(vector)


class InvaderSwarm(System):
    """Control the swarm of things that are coming down from above!"""

    def __init__(self, app):
        super(InvaderSwarm, self).__init__(app)
        self.app = app
        self.swarm_speed = 1
        self.swarm_direction = 1
        self.last_update = 0
        self.update_frequency = 100  # miliseconds
        self.move_down = False

    def update(self):
        if not self.app.playing:
            return
        if self.app.now() - self.last_update > self.update_frequency:
            # Only run once per second
            invaders = get_entities_by_component(self.app.entities, Invader)

            # Check X boundry for invaders
            hit_left = False
            hit_right = False
            for invader in invaders:
                transform = invader.get_component(Transform)
                box = invader.get_component(Box)
                right_edge = transform.position.x + box.width
                left_edge = transform.position.x
                hit_left = left_edge <= 0
                hit_right = right_edge >= self.app.width - 1
                if (hit_left or hit_right):
                    # Hit wall so exit loop
                    break

            # Whether to move down or not this update
            if (hit_left or hit_right) and not self.move_down:
                self.swarm_direction = 1 if hit_left else -1
                self.move_down = True
                x_mult = 0
                y_mult = 2
            else:
                self.move_down = False
                x_mult = 1
                y_mult = 0

            # Move invaders
            for invader in invaders:
                transform = invader.get_component(Transform)
                box = invader.get_component(Box)
                move_vector = Vector2(
                    self.swarm_direction * self.swarm_speed * x_mult,
                    box.height * y_mult)
                transform.translate(move_vector)

            # Check bottom hit
            for invader in invaders:
                transform = invader.get_component(Transform)
                box = invader.get_component(Box)
                if transform.position.y + box.height >= self.app.height - 1:
                    self.app.lose()

            self.last_update = self.app.now()


class Renderer(System):
    """Render things to the game screen"""

    def draw(self):
        if not self.app.playing:
            return
        for entity in self.app.entities.values():
            transform = entity.get_component(Transform)
            box = entity.get_component(Box)
            if transform and box:
                left = transform.position.x
                right = transform.position.x + box.width
                top = transform.position.y
                bottom = transform.position.y + box.height
                fill = entity.get_component(Fill)
                outline = entity.get_component(Outline)
                if fill:
                    pyxel.rect(left, bottom, right, top, fill.color)
                if outline:
                    pyxel.rectb(left, bottom, right, top, outline.color)
