import pygame
import math

from background import screen

player_swing = False

sword_swing = pygame.image.load('melee2/frame_22_swing.png').convert_alpha()
sword_swing = pygame.transform.scale(sword_swing, (150, 150))

frame_count = 0
# Cooldown for the player's swing. actually it is how long you want the animation to last
swing_cooldown = 15


# pass True if player pressed space bar (from main.py)
def swing_status(status):
    global player_swing

    if status:
        player_swing = True
    else:
        player_swing = False


def player_melee(p):
    global swing_cooldown
    global frame_count
    global player_swing

    if swing_cooldown <= 0:
        player_swing = False
        swing_cooldown = 15
        frame_count = 1

    if swing_cooldown > 0:
        if player_swing:
            # Calculate the position of the sword based on the player's position and the frame count
            angle = (frame_count / 60) * 360  # Calculate the angle around the player
            radius = 0  # Distance from player to sword
            sword_x = p.player_x + radius * math.cos(math.radians(angle))
            sword_y = p.player_y + radius * math.sin(math.radians(angle))

            # Rotate the sword image around its center point
            #magic numbers explanations: 10 is for speed of rotation, 60 and 65 are for centering the sword around the player
            #60 and 65 are just numbers I played around with to eyeball the center
            rotated_sword = pygame.transform.rotate(sword_swing, -angle*10)
            sword_center = sword_swing.get_rect(center=(sword_x+60, sword_y+65))
            rotated_rect = rotated_sword.get_rect(center=sword_center.center)

            # Blit the rotated sword image at the calculated position
            screen.blit(rotated_sword, rotated_rect)

            swing_cooldown -= 1

    frame_count += 1
    if frame_count + 1 > 60:
        frame_count = 0
