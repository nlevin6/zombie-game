import pygame

from background import screen

zombie_animation_up = [pygame.image.load('zombie/zombie_walk1_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk1_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk1_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk1_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk1_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk2_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk2_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk2_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk2_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk2_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk3_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk3_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk3_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk3_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk3_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk4_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk4_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk4_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk4_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk4_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk5_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk5_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk5_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk5_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk5_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk6_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk6_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk6_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk6_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk6_u.png').convert_alpha(),
                       ]
zombie_animation_down = [pygame.image.load('zombie/zombie_walk1_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_d.png').convert_alpha(),
                         ]
zombie_animation_left = [pygame.image.load('zombie/zombie_walk1_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_l.png').convert_alpha(),
                         ]
zombie_animation_right = [pygame.image.load('zombie/zombie_walk1_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk1_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk1_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk1_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk1_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk2_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk2_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk2_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk2_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk2_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk3_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk3_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk3_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk3_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk3_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk4_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk4_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk4_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk4_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk4_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk5_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk5_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk5_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk5_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk5_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk6_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk6_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk6_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk6_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk6_r.png').convert_alpha(),
                          ]
frame_count = 0


def draw_zombie(z, p, max_zombies):
    global frame_count

    frame_count += 1
    if frame_count + 1 > 30:  # 30 frames to cycle through

        frame_count = 0

    # calculate distance between zombie and player using the pythagorean theorem
    dist_x = z.get_enemy_x() - p.get_player_x()
    dist_y = z.get_enemy_y() - p.get_player_y()-10
    dist = (dist_x ** 2 + dist_y ** 2) ** 0.5
    #hitbox size
    fake_hitbox_distance = 50

    # move zombie towards player position if not too close
    if dist > fake_hitbox_distance:
        if abs(dist_x) > abs(dist_y):
            if z.get_enemy_x() < p.get_player_x():
                z.enemy_x_change = z.move_speed
                screen.blit(zombie_animation_right[0], (z.enemy_x, z.enemy_y))
            else:
                z.enemy_x_change = -z.move_speed
                screen.blit(zombie_animation_left[0], (z.enemy_x, z.enemy_y))
            z.enemy_y_change = 0
        else:
            if z.get_enemy_y() < p.get_player_y():
                z.enemy_y_change = z.move_speed
                screen.blit(zombie_animation_down[0], (z.enemy_x, z.enemy_y))
            else:
                z.enemy_y_change = -z.move_speed
                screen.blit(zombie_animation_up[0], (z.enemy_x, z.enemy_y))
            z.enemy_x_change = 0


    else:
        z.enemy_x_change = 0
        z.enemy_y_change = 0

        # Face the direction of the player
        if abs(dist_x) > abs(dist_y):
            if z.get_enemy_x() < p.get_player_x():
                screen.blit(zombie_animation_right[0], (z.enemy_x, z.enemy_y))
            else:
                screen.blit(zombie_animation_left[0], (z.enemy_x, z.enemy_y))
        else:
            if z.get_enemy_y() < p.get_player_y():
                screen.blit(zombie_animation_down[0], (z.enemy_x, z.enemy_y))
            else:
                screen.blit(zombie_animation_up[0], (z.enemy_x, z.enemy_y))

    z.enemy_y += z.enemy_y_change
    z.enemy_x += z.enemy_x_change


def enemy_move_limits(e):
    #  set fireplace limits
    if 785 <= e.enemy_x <= 995 and e.enemy_y >= 695:  # top fireplace
        e.enemy_y = 695

    if e.enemy_y >= 710 and 775 >= e.enemy_x >= 770:  # west wall
        e.enemy_x = 770

    if e.enemy_y >= 710 and 1010 >= e.enemy_x >= 1005:  # east wall
        e.enemy_x = 1010