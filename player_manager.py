import pygame
from player import Player
from background import screen

player_animation_right = [pygame.image.load('player/player_walk1_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk1_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk1_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk1_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk1_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk2_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk2_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk2_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk2_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk2_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk3_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk3_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk3_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk3_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk3_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk4_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk4_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk4_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk4_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk4_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk5_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk5_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk5_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk5_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk5_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk6_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk6_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk6_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk6_r.png').convert_alpha(),
                          pygame.image.load('player/player_walk6_r.png').convert_alpha(),
                          ]
player_animation_left = [pygame.image.load('player/player_walk1_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_l.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_l.png').convert_alpha(),
                         ]
player_animation_up = [pygame.image.load('player/player_walk1_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk1_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk1_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk1_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk1_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk2_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk2_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk2_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk2_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk2_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk3_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk3_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk3_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk3_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk3_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk4_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk4_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk4_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk4_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk4_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk5_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk5_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk5_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk5_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk5_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk6_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk6_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk6_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk6_u.png').convert_alpha(),
                       pygame.image.load('player/player_walk6_u.png').convert_alpha(),
                       ]
player_animation_down = [pygame.image.load('player/player_walk1_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk1_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk2_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk3_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk4_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk5_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_d.png').convert_alpha(),
                         pygame.image.load('player/player_walk6_d.png').convert_alpha(),
                         ]

frame_count = 0

player_standing_still_right = pygame.image.load('player/player_walk1_r.png').convert_alpha()
player_standing_still_left = pygame.image.load('player/player_walk1_l.png').convert_alpha()
player_standing_still_up = pygame.image.load('player/player_walk1_u.png').convert_alpha()
player_standing_still_down = pygame.image.load('player/player_walk1_d.png').convert_alpha()



pygame.font.init()

custom_font = pygame.font.SysFont('EightBitDragon-anqx.ttf', 80)

right = False
left = False
up = False
down = False

still_right = False
still_left = False
still_up = True
still_down = False


def player_money(p):
    coin = pygame.image.load('player/coin2.png').convert_alpha()
    coin = pygame.transform.scale(coin, (50, 50))
    screen.blit(coin, (200, 900))
    text_surface = custom_font.render(str(Player.get_money(p)), True, (255, 255, 255))
    screen.blit(text_surface, (250, 900))

def set_animation_status(right_status, left_status, up_status, down_status):
    global right
    global left
    global up
    global down

    global still_right
    global still_left
    global still_up
    global still_down

    if right_status:
        right = True
        left = False
        up = False
        down = False
        still_right = False
        still_left = False
        still_up = False
        still_down = False

    if left_status:
        right = False
        left = True
        up = False
        down = False
        still_right = False
        still_left = False
        still_up = False
        still_down = False

    if up_status:
        right = False
        left = False
        up = True
        down = False
        still_right = False
        still_left = False
        still_up = False
        still_down = False

    if down_status:
        right = False
        left = False
        up = False
        down = True
        still_right = False
        still_left = False
        still_up = False
        still_down = False


def drawHat(p, hatImg):
    if (not isinstance(hatImg, pygame.Surface)):
        return
    hatImg = pygame.transform.scale(hatImg, (50, 50))
    if right:
        hatImg = pygame.transform.rotate(hatImg, -90)
        screen.blit(hatImg, (p.player_x + 60, p.player_y + 30))
    elif left:
        hatImg = pygame.transform.rotate(hatImg, 90)
        screen.blit(hatImg, (p.player_x, p.player_y + 30))
    elif up:

        screen.blit(hatImg, (p.player_x + 30, p.player_y))
    elif down:
        hatImg = pygame.transform.rotate(hatImg, 180)
        screen.blit(hatImg, (p.player_x + 40, p.player_y + 60))
    elif still_right:
        hatImg = pygame.transform.rotate(hatImg, -90)
        screen.blit(hatImg, (p.player_x + 60, p.player_y + 30))
    elif still_left:
        hatImg = pygame.transform.rotate(hatImg, 90)
        screen.blit(hatImg, (p.player_x, p.player_y + 30))
    elif still_up:

        screen.blit(hatImg, (p.player_x + 30, p.player_y))
    else:
        hatImg = pygame.transform.rotate(hatImg, -180)
        screen.blit(hatImg, (p.player_x + 40, p.player_y + 60))


def set_player_still_direction(right_status, left_status, up_status, down_status):
    global still_right
    global still_left
    global still_up
    global still_down

    global right
    global left
    global up
    global down

    if right_status:
        still_right = True
        still_left = False
        still_up = False
        still_down = False
        right = False
        left = False
        up = False
        down = False

    if left_status:
        still_right = False
        still_left = True
        still_up = False
        still_down = False
        right = False
        left = False
        up = False
        down = False

    if up_status:
        still_right = False
        still_left = False
        still_up = True
        still_down = False
        right = False
        left = False
        up = False
        down = False

    if down_status:
        still_right = False
        still_left = False
        still_up = False
        still_down = True
        right = False
        left = False
        up = False
        down = False


def draw_player(p):
    global frame_count
    if right:
        screen.blit(player_animation_right[frame_count], (p.player_x, p.player_y))
    elif left:
        screen.blit(player_animation_left[frame_count], (p.player_x, p.player_y))
    elif up:
        screen.blit(player_animation_up[frame_count], (p.player_x, p.player_y))
    elif down:
        screen.blit(player_animation_down[frame_count], (p.player_x, p.player_y))
    elif still_right:
        screen.blit(player_standing_still_right, (p.player_x, p.player_y))
    elif still_left:
        screen.blit(player_standing_still_left, (p.player_x, p.player_y))
    elif still_up:
        screen.blit(player_standing_still_up, (p.player_x, p.player_y))
    else:
        screen.blit(player_standing_still_down, (p.player_x, p.player_y))

    frame_count += 1
    if frame_count + 1 > 30:  # 30 frames to cycle through
        frame_count = 0


def player_move_limits(p):
    if p.player_x <= 475:  # set player limit on west wall
        p.player_x = 475

    if p.player_x >= 1260:  # set player limit in east wall
        p.player_x = 1260

    if p.player_y >= 765:  # set player limit in south wall
        p.player_y = 765

    if p.player_y <= 230:  # set player limit in north wall
        p.player_y = 230

    if p.player_y <= 315 and p.player_x <= 635:  # set player limit on the jog north-west
        p.player_y = 315  # bottom wall

    if p.player_y <= 300 and p.player_x <= 645:  # set player limit on the jog north-west
        p.player_x = 645  # top wall

    if p.player_y <= 315 and p.player_x >= 1100:  # set player limit in the jog north-east
        p.player_y = 315  # bottom wall

    if p.player_y <= 300 and p.player_x >= 1090:
        p.player_x = 1090  # top wall

    #  set fireplace limits
    if 765 <= p.player_x <= 975 and p.player_y >= 675:  # top fireplace
        p.player_y = 675

    if p.player_y >= 690 and 755 >= p.player_x >= 750:  # west wall
        p.player_x = 750

    if p.player_y >= 690 and 990 >= p.player_x >= 985:  # east wall
        p.player_x = 990
