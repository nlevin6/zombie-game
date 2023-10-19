import pygame

from background import screen

boss_animation_right = [pygame.image.load('boss/skeleton-move_0.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_1.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_2.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_3.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_4.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_5.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_6.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_7.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_8.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_9.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_10.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_11.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_12.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_13.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_14.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_15.png').convert_alpha(),
                        pygame.image.load('boss/skeleton-move_16.png').convert_alpha(),
                        ]
boss_animation_down = [pygame.image.load('boss/skeleton-move_d0.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d1.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d2.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d3.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d4.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d5.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d6.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d7.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d8.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d9.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d10.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d11.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d12.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d13.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d14.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d15.png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_d16.png').convert_alpha(),
                       ]
boss_animation_left = [pygame.image.load('boss/skeleton-move_l0 (1).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (2).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (3).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (4).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (5).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (6).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (7).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (8).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (9).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (10).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (11).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (12).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (13).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (14).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (15).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (16).png').convert_alpha(),
                       pygame.image.load('boss/skeleton-move_l0 (17).png').convert_alpha(),
                       ]
boss_animation_up = [pygame.image.load('boss/skeleton-move_u0 (1).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (2).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (3).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (4).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (5).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (6).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (7).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (8).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (9).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (10).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (11).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (12).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (13).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (14).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (15).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (16).png').convert_alpha(),
                     pygame.image.load('boss/skeleton-move_u0 (17).png').convert_alpha(),
                     ]
frame_count = 0


def draw_boss(z, p):
    global frame_count

    frame_count += 1
    if frame_count + 1 > 17:  # 30 frames to cycle through

        frame_count = 0

    # calculate distance between boss and player using the pythagorean theorem
    dist_x = z.get_boss_x() - p.get_player_x()
    dist_y = z.get_boss_y() - p.get_player_y() - 10
    dist = (dist_x ** 2 + dist_y ** 2) ** 0.5
    # hitbox size
    fake_hitbox_distance = 190

    # move boss towards player position if not too close
    if dist > fake_hitbox_distance:
        if abs(dist_x) > abs(dist_y):
            if z.get_boss_x() < p.get_player_x():
                z.boss_x_change = z.move_speed
                screen.blit(boss_animation_right[frame_count], (z.boss_x, z.boss_y))
            else:
                z.boss_x_change = -z.move_speed
                screen.blit(boss_animation_left[frame_count], (z.boss_x, z.boss_y))
            z.boss_y_change = 0
        else:
            if z.get_boss_y() < p.get_player_y():
                z.boss_y_change = z.move_speed
                screen.blit(boss_animation_down[frame_count], (z.boss_x, z.boss_y))
            else:
                z.boss_y_change = -z.move_speed
                screen.blit(boss_animation_up[frame_count], (z.boss_x, z.boss_y))
            z.boss_x_change = 0


    else:
        z.boss_x_change = 0
        z.boss_y_change = 0

        # Face the direction of the player
        if abs(dist_x) > abs(dist_y):
            if z.get_boss_x() < p.get_player_x():
                screen.blit(boss_animation_right[frame_count], (z.boss_x, z.boss_y))
            else:
                screen.blit(boss_animation_left[frame_count], (z.boss_x, z.boss_y))
        else:
            if z.get_boss_y() < p.get_player_y():
                screen.blit(boss_animation_down[frame_count], (z.boss_x, z.boss_y))
            else:
                screen.blit(boss_animation_up[frame_count], (z.boss_x, z.boss_y))

    z.boss_y += z.boss_y_change
    z.boss_x += z.boss_x_change


def boss_move_limits(e):
    #  set fireplace limits
    if 785 <= e.boss_x <= 995 and e.boss_y >= 695:  # top fireplace
        e.boss_y = 695

    if e.boss_y >= 710 and 775 >= e.boss_x >= 770:  # west wall
        e.boss_x = 770

    if e.boss_y >= 710 and 1010 >= e.boss_x >= 1005:  # east wall
        e.boss_x = 1010
