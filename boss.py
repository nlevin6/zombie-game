import pygame
from datetime import datetime, timedelta
import random

class Boss(pygame.sprite.Sprite):
    move_speed = 0
    hp = 10

    def __init__(self, boss_x, boss_y, boss_x_change, boss_y_change, move_speed):
        super().__init__()
        self.hp = 10
        self.move_speed = move_speed
        self.boss_x = boss_x
        self.boss_y = boss_y
        self.boss_x_change = boss_x_change
        self.boss_y_change = boss_y_change
        self.rect = pygame.Rect(472.5, 472.5, 200, 200)
        self.invincible_until = datetime.now()

    def get_boss_x(self):
        return self.boss_x

    def get_boss_y(self):
        return self.boss_y

    def takeDmg(self, boss):
        self.hp = self.hp - boss.dmg

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
