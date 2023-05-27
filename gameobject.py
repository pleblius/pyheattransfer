class GameObject:
    """A generic abstract GameObject containing attributes and methods to be implemented by subclasses"""
    def __init__(self, name):
        self.name = name
        self.location = ()
        self.size = ()
        self.moving = False
        self.isExpired = False

    def update(self):
        """Update the state of the GameObject"""
        pass

    def draw(self, surface):
        """Define how the GameObject should draw itself"""
        pass
