# import scope
from typing import Callable
import pygame, sys
from sprites import index
import random

# scope of variables
pygame.init()
clock = pygame.time.Clock()

size = width, height = 900, 600
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Coin Rush")
pygame.display.set_icon(index.coin_sprite['coin_0'])

# Scope of classes and functions
class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.acount = 0

        self.animation = index.player_sprites['run']
        self.image = self.animation[0]

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 400

    def update(self):
        self.acount += 1
        if self.acount == len(self.animation):
            self.acount = 0
        self.image = self.animation[self.acount]

class ObstaclesSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animation = index.objects_sprites['obstacles']
        self.image = self.animation[0]

        self.rect = self.image.get_rect()

        self.rect.x = 1200
        self.rect.y = 475

    def update(self):
        self.acount = random.randrange(0, len(index.objects_sprites['obstacles']))
        if self.acount == 2 or self.acount == 1:
            self.rect.y = 515
        else:
            self.rect.y = 475
        self.image = self.animation[self.acount]


# basic menu
def menu(game: Callable):
    button_play = index.buttons_sprites['play']
    button_quit = index.buttons_sprites['quit']

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        left, _, _ = pygame.mouse.get_pressed()

        cursor_position = pygame.mouse.get_pos()

        # button animation
        if cursor_position[0] > 348 and cursor_position[0] < 449 and cursor_position[1] > 221 \
            and cursor_position[1] < 279:
            screen.blit(button_play[1], (320, 200))

            if left:
                game()
        else:
            screen.blit(button_play[0], (320, 200))
        
        if cursor_position[0] > 348 and cursor_position[0] < 449 and cursor_position[1] > 309 \
            and cursor_position[1] < 390:
            screen.blit(button_quit[1], (320, 290))

            if left:
                sys.exit()

        else:
            screen.blit(button_quit[0], (320, 290))
        pygame.display.flip()


# game looping
def game():
    plant_pos_x, plant_pos_y = 0, 550

    group_player = pygame.sprite.Group()
    player_sprite = PlayerSprite()
    group_player.add(player_sprite)

    group_obstacles = pygame.sprite.Group()
    obstacles_sprite = ObstaclesSprite()
    group_obstacles.add(obstacles_sprite)

    jumpcount = 0
    jumpstate = 0

    move_rigth = 10
    move_left = 10

    seconds_counter = 5
    txt=f'{seconds_counter}'                                 
    pygame.font.init()                                
    fonte=pygame.font.get_default_font()             
    fontesys=pygame.font.SysFont(fonte, 60)           
    txttela = fontesys.render(txt, 1, (255,255,255))  
    screen.blit(txttela, (width / 2, height / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jumpstate = 1
                    player_sprite.animation = index.player_sprites['jump']

        if seconds_counter > 1:
            screen.fill(black)
            txt=f'{seconds_counter}'                                          
            txttela = fontesys.render(txt, 1, (255,255,255))  
            screen.blit(txttela, (width / 2, height / 2))
            pygame.display.update()

            seconds_counter -= 1
            pygame.time.delay(1000)
            continue

        # Movement functions
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if not player_sprite.rect.x >= 750:
                player_sprite.rect.x += move_rigth
                
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            if not player_sprite.rect.x <= -20:
                player_sprite.rect.x -= move_left

        if jumpstate:
            move_rigth = 60
            move_left = 60
            jumpcount += 1
            if jumpcount < 4:
                player_sprite.rect.y -= 120
            else:
                player_sprite.rect.y += 60

            if jumpcount > 8:
                move_rigth = 10
                move_left = 10
                jumpstate = 0
                jumpcount = 0
                player_sprite.animation = index.player_sprites['run']


        if player_sprite.rect.colliderect(obstacles_sprite.rect):
            menu(game)

        obstacles_sprite.rect.x -= move_left
        if obstacles_sprite.rect.x < -300:
            obstacles_sprite.update()
            obstacles_sprite.rect.x = 1200

        screen.fill(black)

        # background
        screen.blit(index.backgrounds_image[0], (0, 0))

        group_obstacles.draw(screen)

        group_player.draw(screen)
        group_player.update()

        for i in range(0, 1061, 265):
            if plant_pos_x == -266:
                plant_pos_x = 0

            screen.blit(index.plant_sprites[0], (plant_pos_x + i, plant_pos_y))

        pygame.display.update()

        plant_pos_x -= 2

        clock.tick(60)

if __name__ == '__main__':
    menu(game=game)