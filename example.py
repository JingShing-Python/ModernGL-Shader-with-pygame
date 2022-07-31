import pygame
from pygame.locals import *
from crt_shader import Graphic_engine
from settings import *

# pygame initialize
pygame.init()
clock = pygame.time.Clock()

# as usual you will create a display and give it a name
# i named my display as screen
# and you need to give it a Surface to replace old display
screen = pygame.Surface(VIRTUAL_RES).convert((255, 65282, 16711681, 0))
# you need to give your display OPENGL flag to blit screen using OPENGL
pygame.display.set_mode(REAL_RES, DOUBLEBUF|OPENGL)

# init shader class
crt_shader =  Graphic_engine(screen)

#MAIN LOOP
while (1):
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()

    # you need to put a image in your folder
    img = pygame.image.load('image.png').convert()
    # if you want to render a image on display just blit on screen
    screen.blit(img, (0, 0))

    # never forget to render your shader
    crt_shader()
    clock.tick(FPS)