"""An ECS implementation of Space Invaders using the Pyxel engine"""
import time

import pyxel

from space_invaders.vectors import Vector2
from space_invaders.entities import Entity
from space_invaders.components import (Player, Invader, Transform, Box, Fill,
                                       Outline)
from space_invaders.systems import Input, InvaderSwarm, Renderer


class App:
    """Pyxel App"""

    def __init__(self):
        self.entities = {}
        self.timedelta = 0
        self.last_update = 0
        self.padding = 4
        self.width = 160
        self.height = 120
        self.playing = True

        # Create player entity
        player_size = self.width / 16
        player_start = Vector2(
            round(self.width / 2), self.height - player_size - self.padding)
        player_fill = 13
        player_outline = 6
        player = Entity()
        player.add_component(Player())
        player.add_component(Transform(position=player_start))
        player.add_component(Box(width=player_size, height=player_size))
        player.add_component(Fill(player_fill))
        player.add_component(Outline(player_outline))
        self.entities[player.uid] = player

        # Create Invader entities
        invader_size = 4
        invader_color = 3
        invader_cols = 8
        invader_rows = 4
        x_start = (self.width - invader_size * invader_cols * 3) / 2

        for row in range(0, invader_rows):
            for col in range(0, invader_cols):
                invader = Entity()
                invader_position = Vector2(invader_size * col * 3 + x_start,
                                           invader_size * row * 3)
                invader.add_component(Invader())
                invader.add_component(Transform(position=invader_position))
                invader.add_component(
                    Box(width=invader_size, height=invader_size))
                invader.add_component(Fill(invader_color))
                self.entities[invader.uid] = invader

        # Add systems to app context
        self.systems = []
        self.systems.append(Input(self))
        self.systems.append(InvaderSwarm(self))
        self.systems.append(Renderer(self))

        pyxel.init(self.width, self.height)
        pyxel.run(self.update, self.draw)

    def lose(self):
        pyxel.cls(7)
        pyxel.text(self.width / 2, self.height / 2, 'GAME OVER', 1)
        self.playing = False

    def now(self):
        """Returns the current time in microseconds"""
        return int(round(time.time() * 1000))

    def update(self):
        """Update function passed into Pyxel"""
        self.timedelta = self.now() - self.last_update / 1000
        for system in self.systems:
            system.update()
        self.last_update = self.now()

    def draw(self):
        """Draw function passed into Pyxel"""
        if not self.playing:
            return
        pyxel.cls(0)
        for system in self.systems:
            system.draw()
