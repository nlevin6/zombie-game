import pygame
from datetime import datetime, timedelta
import random

class Enemy(pygame.sprite.Sprite):
    move_speed = 0
    hp = 0

    def __init__(self, enemy_x, enemy_y, enemy_x_change, enemy_y_change, move_speed):
        super().__init__()
        self.hp = 3
        self.move_speed = move_speed
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.enemy_x_change = enemy_x_change
        self.enemy_y_change = enemy_y_change
        self.rect = pygame.Rect(472.5, 472.5, 55, 55)
        self.invincible_until = datetime.now()
    
    def respawn(self, move_speed, x,y):
        if self.hp == 0:
            self.hp = 3
        self.x, self.y = (x,y)
        self.move_speed = move_speed
        return self

    def get_enemy_x(self):
        return self.enemy_x

    def get_enemy_y(self):
        return self.enemy_y

    # use this method to reset each enemy that died (reached 0 hp), to re-spawn them on the screen at a random location
    def enemy_reset(self, x, y):
        self.enemy_x = x
        self.enemy_y = y
        move_speed = random.randrange(1, 3)
        self.move_speed = move_speed
        if self.hp == 0:
            self.hp = 3

    def takeDmg(self, enemy):
        self.hp = self.hp - enemy.dmg

    def _can_take_damage(self):
        if datetime.now() < self.invincible_until:
            return False
        return True

    def attack_check(self, damage):
        if self._can_take_damage():
            if damage> self.hp:
                self.hp=0
            else:
             self.hp -= damage
            self.invincible_until = datetime.now() + timedelta(seconds=0)
