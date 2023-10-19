import pygame

# screen size
pygame.init()
info = pygame.display.Info()
#WIDTH, HEIGHT = 1920, 1080
WIDTH, HEIGHT = info.current_w, info.current_h

# draw screen and import floor
screen = pygame.display.set_mode((WIDTH, HEIGHT))
floor = pygame.image.load('floor/floor.png').convert_alpha()

# import walls
wall_corner_bot_left = pygame.image.load('walls/wall-corner-bottom-left.png').convert_alpha()
wall_corner_bot_right = pygame.image.load('walls/wall-corner-bottom-right.png').convert_alpha()
wall_corner_top_left = pygame.image.load('walls/wall-corner-top-left.png').convert_alpha()
wall_corner_top_right = pygame.image.load('walls/wall-corner-top-right.png').convert_alpha()
wall_horiz = pygame.image.load('walls/wall-horizontal.png').convert_alpha()
wall_vert = pygame.image.load('walls/wall-vertical.png').convert_alpha()

# import fireplace stuff
fp_floor = pygame.image.load('floor/fireplace_floor.png').convert_alpha()

# door
door = pygame.image.load('door/door.png').convert_alpha()

# table
table = pygame.image.load('npc/table.png').convert_alpha()
table_shadow = pygame.image.load('npc/table_shadow.png').convert_alpha()

#  resize table
table = pygame.transform.rotozoom(table, 90, 0.15)  # rotate 90 degrees, scale 15%
table_shadow = pygame.transform.rotozoom(table_shadow, 90, 0.20)

# resize walls
wall_corner_top_left = pygame.transform.scale(wall_corner_top_left, (85, 85))
wall_corner_bot_right = pygame.transform.scale(wall_corner_bot_right, (85, 85))
wall_corner_top_right = pygame.transform.scale(wall_corner_top_right, (85, 85))
wall_corner_bot_left = pygame.transform.scale(wall_corner_bot_left, (85, 85))
wall_horiz = pygame.transform.scale(wall_horiz, (85, 25))
wall_vert = pygame.transform.scale(wall_vert, (25, 85))

# resize door
door = pygame.transform.scale(door, (100, 16))

fire_animation = [pygame.image.load('fire/1_0.png').convert_alpha(),
                  pygame.image.load('fire/1_1.png').convert_alpha(),
                  pygame.image.load('fire/1_2.png').convert_alpha(),
                  pygame.image.load('fire/1_3.png').convert_alpha(),
                  pygame.image.load('fire/1_4.png').convert_alpha(),
                  pygame.image.load('fire/1_5.png').convert_alpha(),
                  pygame.image.load('fire/1_6.png').convert_alpha(),
                  pygame.image.load('fire/1_7.png').convert_alpha(),
                  pygame.image.load('fire/1_8.png').convert_alpha(),
                  pygame.image.load('fire/1_9.png').convert_alpha(),
                  pygame.image.load('fire/1_11.png').convert_alpha(),
                  pygame.image.load('fire/1_12.png').convert_alpha(),
                  pygame.image.load('fire/1_13.png').convert_alpha(),
                  pygame.image.load('fire/1_14.png').convert_alpha(),
                  ]
frame_count = 0


# makes animation for fire
def draw_fire():
    global frame_count
    screen.blit(fire_animation[frame_count], (810, 720))
    screen.blit(fire_animation[frame_count], (830, 720))
    screen.blit(fire_animation[frame_count], (850, 720))
    screen.blit(fire_animation[frame_count], (870, 720))
    screen.blit(fire_animation[frame_count], (890, 720))
    screen.blit(fire_animation[frame_count], (910, 720))
    screen.blit(fire_animation[frame_count], (930, 720))
    screen.blit(fire_animation[frame_count], (950, 720))

    screen.blit(fire_animation[frame_count], (820, 710))
    screen.blit(fire_animation[frame_count], (840, 710))
    screen.blit(fire_animation[frame_count], (880, 710))
    screen.blit(fire_animation[frame_count], (900, 710))
    screen.blit(fire_animation[frame_count], (940, 710))
    frame_count += 1
    if frame_count + 1 > 14:  # 14 frames cycled through
        frame_count = 0


def draw_table():
    screen.blit(table_shadow, (1340, 520))
    screen.blit(table, (1350, 535))


def floor_builder():
    # TODO: add for loops to make this look better

    # screen.blit(floor, (500, 255))
    screen.blit(floor, (670, 255))
    screen.blit(floor, (840, 255))
    screen.blit(floor, (1010, 255))
   # screen.blit(floor, (1180, 255))

    screen.blit(floor, (500, 340))
    screen.blit(floor, (670, 340))
    screen.blit(floor, (840, 340))
    screen.blit(floor, (1010, 340))
    screen.blit(floor, (1180, 340))

    screen.blit(floor, (500, 425))
    screen.blit(floor, (670, 425))
    screen.blit(floor, (840, 425))
    screen.blit(floor, (1010, 425))
    screen.blit(floor, (1180, 425))

    screen.blit(floor, (500, 510))
    screen.blit(floor, (670, 510))
    screen.blit(floor, (840, 510))
    screen.blit(floor, (1010, 510))
    screen.blit(floor, (1180, 510))
    screen.blit(floor, (1350, 510))

    screen.blit(floor, (500, 595))
    screen.blit(floor, (670, 595))
    screen.blit(floor, (840, 595))
    screen.blit(floor, (1010, 595))
    screen.blit(floor, (1180, 595))
    screen.blit(floor, (1350, 595))

    screen.blit(floor, (500, 680))
    screen.blit(floor, (670, 680))
    screen.blit(floor, (840, 680))
    screen.blit(floor, (1010, 680))
    screen.blit(floor, (1180, 680))

    screen.blit(floor, (500, 765))
    screen.blit(floor, (670, 765))
    # screen.blit(floor, (840, 765))
    screen.blit(floor, (1010, 765))
    screen.blit(floor, (1180, 765))


def wall_builder():
    # walls
    screen.blit(wall_horiz, (500, 315))
    screen.blit(wall_horiz, (730, 230))
    screen.blit(wall_horiz, (1034, 230))
    screen.blit(wall_horiz, (1215, 315))
    screen.blit(wall_horiz, (1400, 485))
    screen.blit(wall_horiz, (1400, 679))
    screen.blit(wall_vert, (1349, 400))
    screen.blit(wall_vert, (1520, 550))
    screen.blit(wall_vert, (1350, 750))
    screen.blit(wall_vert, (475, 400))
    screen.blit(wall_vert, (475, 570))
    screen.blit(wall_vert, (475, 650))
    screen.blit(wall_vert, (475, 730))
    screen.blit(wall_horiz, (1205, 849))
    screen.blit(wall_horiz, (1035, 850))
    screen.blit(wall_horiz, (950, 850))
    screen.blit(wall_horiz, (865, 850))
    screen.blit(wall_horiz, (780, 850))
    screen.blit(wall_horiz, (695, 850))
    screen.blit(wall_horiz, (525, 850))
    screen.blit(wall_horiz, (790, 230))
    screen.blit(wall_horiz, (975, 230))

    # door
    screen.blit(door, (875, 239))

    # corners
    screen.blit(wall_corner_top_left, (475, 315))
    screen.blit(wall_corner_bot_right, (585, 255))
    screen.blit(wall_corner_bot_right, (1460, 618))
    screen.blit(wall_corner_top_left, (645, 230))
    screen.blit(wall_corner_top_right, (1119, 230))
    screen.blit(wall_corner_bot_left, (1180, 255))
    screen.blit(wall_corner_top_right, (1288, 315))
    screen.blit(wall_corner_bot_left, (1350, 425))
    screen.blit(wall_corner_bot_right, (1289, 789))
    screen.blit(wall_corner_bot_left, (475, 790))
    screen.blit(wall_corner_top_right, (1458, 485))
    screen.blit(wall_corner_top_left, (1350, 680))


def build_background():
    screen.fill((0, 0, 0))
    floor_builder()
    draw_fire()
    wall_builder()
    draw_table()
