import pygame
from src.objects.state import State
from src.controller import Controller
from src import view
from src.objects.wall import Wall

pygame.init()
state = State()
controller = Controller(state)
state.add_wall(Wall("wall1"))

#  Basic game loop - gets events from the user and sends them to the controller to perform updates
running = True
while running:
    #  Exit condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #  Other game event conditions
        else:
            controller.handle_event(event)
            view.draw_game(state)


pygame.quit()
