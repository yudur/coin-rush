import pygame

coin_sprite = {
    'coin_0' : pygame.image.load('sprites/coin/coin.png')
}

plant_sprites = [
    pygame.image.load('sprites/plant_sprite/tile000.png'),
    pygame.image.load('sprites/plant_sprite/tile001.png')
]


player_sprites = {
    'run': [
        pygame.image.load('sprites/player/Run__000.png'),
        pygame.image.load('sprites/player/Run__001.png'),
        pygame.image.load('sprites/player/Run__002.png'),
        pygame.image.load('sprites/player/Run__003.png'),
        pygame.image.load('sprites/player/Run__004.png'),
        pygame.image.load('sprites/player/Run__005.png'),
        pygame.image.load('sprites/player/Run__006.png'),
        pygame.image.load('sprites/player/Run__007.png'),
        pygame.image.load('sprites/player/Run__008.png'),
        pygame.image.load('sprites/player/Run__009.png')
    ],

    'jump': [
        pygame.image.load('sprites/player/Jump__000.png'),
        pygame.image.load('sprites/player/Jump__001.png'),
        pygame.image.load('sprites/player/Jump__002.png'),
        pygame.image.load('sprites/player/Jump__003.png'),
        pygame.image.load('sprites/player/Jump__004.png'),
        pygame.image.load('sprites/player/Jump__005.png'),
        pygame.image.load('sprites/player/Jump__006.png'),
        pygame.image.load('sprites/player/Jump__007.png'),
        pygame.image.load('sprites/player/Jump__008.png'),
        pygame.image.load('sprites/player/Jump__009.png')
    ]
}

objects_sprites = {
    'obstacles': [
        pygame.image.load('sprites/objects/Stone.png'),
        pygame.image.load('sprites/objects/Crate.png'),
        pygame.image.load('sprites/objects/Tree_1.png')
    ]
}

backgrounds_image = [
    pygame.image.load('sprites/background/BG.png')
]

buttons_sprites = {
    'play' : [
        pygame.image.load("sprites/menu_sprites/btn1.png"),
        pygame.image.load("sprites/menu_sprites/btn2.png")
    ],

    'quit' : [
        pygame.image.load("sprites/menu_sprites/quit1.png"),
        pygame.image.load("sprites/menu_sprites/quit2.png")
    ]
}