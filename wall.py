import pygame.draw

from gameobject import GameObject


class Wall(GameObject):
    """A wall game object to conduct heat.

    Defines the game-size, dimensions, and material properties for the wall. When instantiated, the wall
    will be displayed in the window, and can be connected to border objects, which can themselves be connected
    to other wall objects."""
    def __init__(self, name):
        super().__init__(name)
        self.moving = True
        self.properties = ()
        self.borders = ()
        self.tempArray = []

    def update(self):
        """Updates the wall based on the expected game-state for the next frame.

        Adjusts the wall's temperature distribution, properties, and size characteristics depending on any
        changes that have been made to the game state since the last update"""
        pass

    def draw(self, surface):
        """Draws the wall based on its current location, size, and coloring"""
        pygame.draw.rect(surface, pygame.Color('brown'), [100, 100, 100, 100])
