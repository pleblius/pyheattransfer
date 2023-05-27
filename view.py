import pygame
from state import State
"""A module to control the display for the application.
    
Houses all the necessary information and methods to draw the game-state to the screen."""

#  Display window setup and initialization.
width, height = 800, 600    # Pixels
displayWindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("Heat Transfer Application")


def draw_game(state: State):
    displayWindow.fill(pygame.Color('cornsilk'))

    for wall in state.walls:
        wall.draw()
    for boundary in state.boundaries:
        boundary.draw()

    pygame.display.flip()
