import pygame

pygame.init()

#  Basic game loop - gets events from the user and sends them to the controller to perform updates
running = True
while running:
    #  Exit condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

pygame.quit()
