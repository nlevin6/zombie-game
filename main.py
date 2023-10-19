import pygame
import random
from background import build_background
from gameOverScreen import importFont
from enemy import Enemy
from boss import Boss
from enemy_manager import draw_zombie, enemy_move_limits
from boss_manager import draw_boss, boss_move_limits
from lighting import create_light
from player import Player
from player_attacks import player_melee, swing_status
from player_manager import draw_player, set_animation_status, set_player_still_direction, player_move_limits, drawHat, \
    player_money
from healthBar import drawHpBar, drawEnemyHpBar, drawBossHpBar
from gameOverScreen import GameOverScreen
from background import screen
import threading
from shop import buyDmg, drawstat, buySpeed, buyHp, drawInstruction, merchartFirsttime, resetPrice, drawPrice
from controls import drawControls
from pygame import mixer

pygame.init()
running = True
clock = pygame.time.Clock()
blood_image = pygame.image.load("blood splatter.png")
merchart = pygame.image.load("InstructionPicutre/merchantBlackPicture.png")
merchart = pygame.transform.scale(merchart, (100, 100))
blood_timers = {}
text_shown = {}
timers = []

mixer.music.load('campfire.mp3')
mixer.music.play(-1)
player_steps = mixer.Sound('steps_player.mp3')

hat = [0, pygame.image.load('hatfolder/duckyHat.png').convert_alpha(),
       pygame.image.load('hatfolder/cowboy_Hat.png').convert_alpha()
       ]

p = Player(870, 500, 0, 0, 0)  # spawn player at 870, 500 with a change of 0 for x and y
boss = Boss(450, 400, 0, 0, 1)
# e1 = Enemy(500, 500, 0, 0)  # create test zombie
enemies = []  # list of enemies
level_active = True
boss_stage = False
current_level = 1
number_of_enemies = 3  # number of enemies to spawn
enemies_counter = number_of_enemies

pygame.font.init()
myfont = pygame.font.SysFont('EightBitDragon-anqx.ttf', 60)
myfont_small = pygame.font.SysFont('EightBitDragon-anqx.ttf', 30)


def spawn_enemy():
    # spawn coordinates for enemies
    # door: 875, 239, window_vert: 485, 485, window_horiz: 1120, 850, window_horiz: 610, 850
    spawn_locations = [(875, 249), (495, 485), (1120, 810), (610, 810)]
    spawn_location = random.choice(spawn_locations)
    x_pos = random.randrange(spawn_location[0] - 10, spawn_location[0] + 10)
    y_pos = random.randrange(spawn_location[1] - 10, spawn_location[1] + 10)
    move_speed = random.uniform(0.5, 3)
    e = Enemy(x_pos, y_pos, 0, 0, move_speed)
    enemies.append(e)


def populate_enemies(num_enemies):
    for i in range(num_enemies):
        # random spawn time between 0.5 and 7 seconds per enemy
        timer = threading.Timer(random.uniform(0.5, 7), spawn_enemy)
        timer.start()


populate_enemies(number_of_enemies)

pressed_keys = set()


def events():
    global running
    global level_active
    global number_of_enemies
    global current_level
    global enemies_counter
    global boss_stage

    keys_pressed = pygame.key.get_pressed()
    # Update player direction based on currently pressed keys
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        p.player_x_change = -p.move_speed
        set_animation_status(False, True, False, False)
    elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        p.player_x_change = p.move_speed
        set_animation_status(True, False, False, False)
    else:
        p.player_x_change = 0

    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        p.player_y_change = -p.move_speed
        set_animation_status(False, False, True, False)
    elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        p.player_y_change = p.move_speed
        set_animation_status(False, False, False, True)
    else:
        p.player_y_change = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # esc button closes the game
                running = False

            # if player presses f, swing animation
            if event.key == pygame.K_SPACE:
                swing_sound = mixer.Sound('swinging.mp3')
                swing_sound.play()
                swing_status(True)
                attackBoss(boss)
                for enemy in enemies:
                    attack(enemy)

            # this is to add hp with o and remove hp with p
            if event.key == pygame.K_RETURN and level_active is False:
                level_active = True
                current_level += 1
                if current_level % 5 == 0 and current_level != 0:
                    boss_stage = True
                else:
                    boss_stage = False

                level = myfont.render('Level ' + str(current_level), False, (255, 255, 255))
                screen.blit(level, (1500, 100))
                number_of_enemies += 2
                enemies_counter = number_of_enemies
                populate_enemies(number_of_enemies)
                # hp ain't going to be free
                # p.heal(1)

            # Buying things from the shop
            if event.key == pygame.K_b and level_active is False:
                buyDmg(p)
            if event.key == pygame.K_n and level_active is False:
                buySpeed(p)
            if event.key == pygame.K_m and level_active is False:
                buyHp(p)

            if event.key == pygame.K_p:
                p.takeDmg(1)
            if event.key == pygame.K_0:
                p.hatIndex = p.hatIndex + 1

        if event.type == pygame.KEYUP:
            p.player_x_change = 0  # stop moving player if key is not pressed anymore
            p.player_y_change = 0

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if p.player_x_change < 0:
                    p.player_x_change = 0
                set_player_still_direction(False, True, False, False)

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if p.player_x_change > 0:
                    p.player_x_change = 0
                set_player_still_direction(True, False, False, False)

            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                if p.player_y_change < 0:
                    p.player_y_change = 0
                set_player_still_direction(False, False, True, False)

            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if p.player_y_change > 0:
                    p.player_y_change = 0
                set_player_still_direction(False, False, False, True)
            set_animation_status(False, False, False, False)  # just in case

    # change player position
    p.player_x += p.player_x_change
    p.player_y += p.player_y_change


def attack(enemy):
    global respawn_counter
    global enemies_counter
    p.rect.x = p.player_x + 50
    p.rect.y = p.player_y + 50
    # the attack hitbox of the player, change this if you want to adjust how far the player can attack
    hitbox_size = 200
    hitbox_left = p.rect.x - hitbox_size // 2
    hitbox_top = p.rect.y - hitbox_size // 2
    hitbox = pygame.Rect(hitbox_left, hitbox_top, hitbox_size, hitbox_size)
    # draw hitbox for testing
    # pygame.draw.rect(screen,(255,255,255),hitbox)
    enemy.rect.x = enemy.enemy_x
    enemy.rect.y = enemy.enemy_y
    if hitbox.colliderect(enemy.rect):
        enemy.attack_check(p.dmg)
        if enemy.hp == 0:
            enemies_counter -= 1
            blood_timers[enemy] = pygame.time.get_ticks()
            respawn_counter += 1
            p.add_money()
    return True


def attackBoss(b):
    global respawn_counter
    global boss_stage
    global enemies_counter
    p.rect.x = p.player_x + 50
    p.rect.y = p.player_y + 50
    # the attack hitbox of the player, change this if you want to adjust how far the player can attack
    hitbox_size = 250
    hitbox_left = p.rect.x - hitbox_size // 2
    hitbox_top = p.rect.y - hitbox_size // 2
    hitbox = pygame.Rect(hitbox_left, hitbox_top, hitbox_size, hitbox_size)
    # draw hitbox for testing
    # pygame.draw.rect(screen,(255,255,255),hitbox)
    b.rect.x = b.boss_x
    b.rect.y = b.boss_y
    if hitbox.colliderect(b.rect) and boss_stage:
        b.attack_check(p.dmg)
        if b.hp == 0:
            blood_timers[b] = pygame.time.get_ticks()
            p.add_big_money()

    return True


def collision(enemy):
    p.rect.x = p.player_x
    p.rect.y = p.player_y
    # screen.blit(hat[1], (p.rect.x, p.rect.y))

    enemy.rect.x = enemy.enemy_x
    enemy.rect.y = enemy.enemy_y
    if p.rect.colliderect(enemy.rect):
        p.hit_check(1)

    return True


def collisionBoss(b):
    p.rect.x = p.player_x
    p.rect.y = p.player_y
    # screen.blit(hat[1], (p.rect.x, p.rect.y))

    b.rect.x = b.boss_x
    b.rect.y = b.boss_y
    if p.rect.colliderect(b.rect):
        p.hit_check(1)

    return True


respawn_counter = 0

def main():
    global respawn_counter
    global number_of_enemies
    global current_level
    global level_active
    global enemies_counter
    global boss_stage

    build_background()

    events()

    if boss_stage:
        boss_move_limits(boss)
        if boss.hp > 0 and level_active:
            draw_boss(boss, p)
            drawBossHpBar(boss)
            collisionBoss(boss)

    level = myfont.render('Level ' + str(current_level), False, (255, 255, 255))
    screen.blit(level, (1500, 100))

    # drawstat(p)
    if level_active is False:
        shop_notification = myfont_small.render('You can now purchase from the shop', False, (0, 153, 51))
        start_notification = myfont_small.render('Press ENTER to start next level', False, (0, 153, 51))
        screen.blit(shop_notification, (1500, 150))
        screen.blit(start_notification, (1500, 180))
        merchartFirsttime(current_level)
        drawPrice(p)

        boss.hp = current_level * 2

        if current_level > 0:
            screen.blit(merchart, (1400, 500))

        for enemy in enemies:
            enemies.remove(enemy)

    player_melee(p)
    draw_player(p)  # pass player object into this method
    player_move_limits(p)  # pass player object
    drawHpBar(p)
    drawHat(p, hat[p.hatIndex % 3])
    player_money(p)
    drawControls()
    for enemy in enemies:
        enemy_move_limits(enemy)
        if enemy.hp > 0:
            max_zombies = len(enemies)
            drawEnemyHpBar(enemy)
            draw_zombie(enemy, p, max_zombies)
            collision(enemy)
        else:
            enemy_die = mixer.Sound('blood.mp3')
            enemy_die.play()
            enemies.remove(enemy)
            if enemies_counter == 0 and level_active:
                level_active = False

            # blood_rect = blood_image.get_rect(center=(enemy.rect.x, enemy.rect.y))
            # if pygame.time.get_ticks() - blood_timers[enemy] < 1000:
            #     screen.blit(blood_image, blood_rect)

    create_light()
    drawInstruction(current_level, p)
    pygame.display.flip()
    clock.tick(50)
    if p.hp <= 0:
        p.player_x = 870
        p.player_y = 500
        GameOverScreen(p, current_level)
        current_level = 0
        number_of_enemies = 1
        level_active = False
        p.money = 0
        resetPrice()


if __name__ == '__main__':
    while running:
        main()
    pygame.quit()
