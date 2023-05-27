import pygame

pygame.init()


#  Display window setup and initialization.
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Heat Transfer Application")

#  Create maps containing all game objects
walls = {}
boundaries = {}
toDelete = []

#  Basic game loop - updates and draws all objects to the display
running = True
while running:
    #  Exit condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #  Update
    window.fill(pygame.Color('cornsilk'))

    for wall in walls:
        wall.update()
    for boundary in boundaries:
        boundary.update()

    #  Draw

    for wall in walls:
        wall.draw()
    for boundary in boundaries:
        boundary.draw()

    #  Display
    pygame.display.flip()

    #  Cleanup
    for obj in toDelete:
        if obj in walls:
            del walls[obj]
        elif obj in boundaries:
            del boundaries[obj]

pygame.quit()
