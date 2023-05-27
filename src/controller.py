from src.state import State
import pygame


class Controller:
    """A class to control game flow and handle user inputs and events.

    A controller object is responsible for dictating the logical flow of the game, making sure
    objects update when necessary and passing user inputs to the proper functions and methods."""
    def __init__(self, state: State):
        self.state = state

    def create_wall(self):
        pass
