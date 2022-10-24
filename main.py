import pygame
import grid
import os

os.environ["SDL_VIDEO_CENTERED"] = '1'
run = True # flag to stop simulation from running
pause = False # pauses simulation
pygame.init()
width, height = 1920, 1080
size = (width, height)
pygame.display.set_caption("CONWAY'S GAME  OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

scale = 20
offset = 1
conwayclass = grid.Grid(scale, offset, width, height, screen)
conwayclass.array_generate()

while run:
    clock.tick(fps)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT: # to end simulation
            run = False
        if event.type==pygame.KEYUP: 
            if event.key==pygame.K_ESCAPE:
                run = False
            if event.key==pygame.K_SPACE:
                pause = not pause

    conwayclass.conway(screen, pause)

    if pygame.mouse.get_pressed()[0]: # handles mouse click to add cell 
        mouseX, mouseY = pygame.mouse.get_pos()
        conwayclass.mouse_handle(mouseX,mouseY)

    pygame.display.update()

pygame.quit()