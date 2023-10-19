import pygame

from background import screen

# import window light
window_light = pygame.image.load('windows/window_light.png').convert_alpha()

# rotate and resize window light
window_light_vert = pygame.transform.rotozoom(window_light, 90, 0.15)
window_light_horiz = pygame.transform.rotozoom(window_light, 180, 0.15)

# import glow
glow = pygame.image.load('fire/glow.png').convert_alpha()

# resize glow
glow = pygame.transform.scale(glow, (216, 216))

# import fireplace
fp = pygame.image.load('floor/fireplace_floor.png').convert_alpha()

# resize fireplace
fp = pygame.transform.scale(fp, (169, 84))

# windows
window_horiz = pygame.image.load('windows/window-horizontal.png').convert_alpha()
window_vert = pygame.image.load('windows/window-vert.png').convert_alpha()

# resize windows
window_vert = pygame.transform.scale(window_vert, (15, 85))
window_horiz = pygame.transform.scale(window_horiz, (85, 15))


def create_light():
    # window lights
    screen.blit(window_light_vert, (484, 475))
    screen.blit(window_light_horiz, (598, 773))
    screen.blit(window_light_horiz, (1105, 773))

    # glow and fireplace
    screen.blit(glow, (810, 685))
    screen.blit(fp, (840, 765))

    # windows
    screen.blit(window_vert, (485, 485))
    screen.blit(window_horiz, (1120, 850))
    screen.blit(window_horiz, (610, 850))
