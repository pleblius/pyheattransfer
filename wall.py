import copy


class Wall:
    """A wall game object to conduct heat.

    Defines the game-size, dimensions, and material properties for the wall. When instantiated, the wall
    will be displayed in the window, and can be connected to border objects, which can themselves be connected
    to other wall objects.
    name should be a string
    size should be a list of [width, height] in pixels
    location should be a list of [x, y] in pixels
    length should be a float in meters
    properties should be a list of [density, heat capacity, conductivity, constant heat generation]"""
    def __init__(self, name: str, size, location, length, properties: []):
        self.name = name
        self.size = copy.copy(size)
        self.location = copy.copy(location)
        self.length = length
        self.properties = copy.copy(properties)
        self.moving = True

    def update(self):
        """Updates the wall based on the expected game-state for the next frame.

        Adjusts the wall's temperature distribution, properties, and size characteristics depending on any
        changes that have been made to the game state since the last update"""
        pass

    def draw(self):
        """Draws the wall based on its current location, size, and coloring"""
        pass