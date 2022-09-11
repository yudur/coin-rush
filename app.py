import pygame, sys


pygame.init()

size = width, height = 900, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Coin Rush")

icon = pygame.image.load('sprites/gold.png')

pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    pygame.display.flip()