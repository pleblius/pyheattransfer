from wall import Wall
from boundary import Boundary


class State:
    """The state class, which as an object functions as the model for the application.

    The state contains the information related to the game state and the methods to
    modify that game information, all of which can then be controlled
    by the controller object and drawn by the view object."""
    def __init__(self):
        self.walls = set()
        self.boundaries = set()

    def add_wall(self, new_wall: Wall):
        self.walls.add(new_wall)

    def add_boundary(self, new_boundary: Boundary):
        self.boundaries.add(new_boundary)

    def start_frame(self):
        pass

    def finish_frame(self):
        pass

    def save_state(self):
        pass

    def load_state(self):
        pass
