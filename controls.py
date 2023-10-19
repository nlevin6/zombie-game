import pygame

from background import screen
from gameOverScreen import importFont

# import images
w_key = pygame.image.load('controls/W.png').convert_alpha()
a_key = pygame.image.load('controls/A.png').convert_alpha()
s_key = pygame.image.load('controls/S.png').convert_alpha()
d_key = pygame.image.load('controls/D.png').convert_alpha()

# resize images

w_keyGame = pygame.transform.scale(w_key, (45, 45))
a_keyGame = pygame.transform.scale(a_key, (45, 45))
s_keyGame = pygame.transform.scale(s_key, (45, 45))
d_keyGame = pygame.transform.scale(d_key, (45, 45))

def drawControls():
    font = importFont(36)
    moveUp = font.render('to move up', False, (200, 0, 0))
    moveDown = font.render('to move down', False, (200, 0, 0))
    moveRight = font.render('to move right', False, (200, 0, 0))
    moveLeft = font.render('to move left', False, (200, 0, 0))
    attack = font.render('SPACE to attack', False, (200, 0, 0))
    hat = font.render('0 to change hat', False, (200, 0, 0))
    screen.blit(moveUp,(155,610))
    screen.blit(w_keyGame,(100,600))

    screen.blit(moveLeft,(155,660))
    screen.blit(a_keyGame,(100,655))

    screen.blit(moveDown,(155,720))
    screen.blit(s_keyGame,(100,710))

    screen.blit(moveRight,(155,780))
    screen.blit(d_keyGame,(100,765))

    screen.blit(attack, (100,820))

    screen.blit(hat, (100,855))
    


