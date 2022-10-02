from typing import Tuple
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

def collision(position_player: Tuple[int, int], position_object: Tuple[int, int]):
    if position_player[0] == position_object[0] and position_player[1] == position_object[1]:
        return True
    else:
        return False

group_player = pygame.sprite.Group()
player_sprite = PlayerSprite()
group_player.add(player_sprite)

jumpcount = 0
jumpstate = 0

seconds_counter = 5
txt=f'{seconds_counter}'                                 
pygame.font.init()                                
fonte=pygame.font.get_default_font()             
fontesys=pygame.font.SysFont(fonte, 60)           
txttela = fontesys.render(txt, 1, (255,255,255))  
screen.blit(txttela, (width / 2, height / 2))

move_rigth = 10
move_left = 10

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
        
        pygame.time.delay(20)

    screen.fill(black)

    group_player.draw(screen)
    group_player.update()

    for i in range(0, 1061, 265):
        if plant_pos_x == -266:
            plant_pos_x = 0

        screen.blit(index.plant_sprites[0], (plant_pos_x + i, plant_pos_y))

    pygame.display.update()

    plant_pos_x -= 2

    clock.tick(30)
    