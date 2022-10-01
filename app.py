import pygame, sys
from sprites import index


pygame.init()
clock = pygame.time.Clock()

size = width, height = 900, 600
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Coin Rush")
pygame.display.set_icon(index.coin_sprite['coin_0'])

plant_pos_x, plant_pos_y = 0, 550

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)

    for i in range(0, 1061, 265):
        if plant_pos_x == -266:
            plant_pos_x = 0

        screen.blit(index.plant_sprites[0], (plant_pos_x + i, plant_pos_y))

    pygame.display.update()

    plant_pos_x -= 2

    clock.tick(60)