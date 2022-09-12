import pygame, sys
from sprites import index


pygame.init()

size = width, height = 900, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Coin Rush")
pygame.display.set_icon(index.coin_sprite['coin_0'])

glass_position_width = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for i in range(len(index.glass_sprites) + 2):
        if i >= 2:
            i = 0

        screen.blit(index.glass_sprites[i], (glass_position_width, 550))
        glass_position_width += 265

    pygame.display.flip()