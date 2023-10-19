import pygame
from datetime import datetime, timedelta
from pygame import mixer


class Player:
    money = 0
    move_speed = 4
    hp = 4
    dmg = 1
    hatIndex=0
    def __init__(self, player_x, player_y, player_x_change, player_y_change, money):
        self.hp = 4
        self.dmg = 1
        self.player_x = player_x
        self.player_y = player_y
        self.player_x_change = player_x_change
        self.player_y_change = player_y_change
        self.animation_loop = 0
        if self.animation_loop == 0:
            self.collidable = True
        self.rect = pygame.Rect(845, 475, 50, 50)
        self.invincible_until = datetime.now()
        self.money = money

    #use this method do add money to the player whenever he kills an enemy
    def add_money(self):
        self.money += 1
    def add_big_money(self):
        self.money += 5

    def get_money(self):
        return self.money

    def _can_take_damage(self):
        if datetime.now() < self.invincible_until:
            return False
        return True

    def hit_check(self, damage):
        if self._can_take_damage():
            self.hp -= damage
            player_moaning = mixer.Sound('get_hurt.mp3')
            player_moaning.play()
            self.invincible_until = datetime.now() + timedelta(seconds=1)

    def get_player_x(self):
        return self.player_x

    def get_player_y(self):
        return self.player_y

    # heal the player byt the number given
    # p.heal(1) to heal 1
    def heal(self, hpNumber):
        self.hp = self.hp + hpNumber

    # removing hp from player by the given number
    # eg: p.takeDmg(1) to take one dmg 
    def takeDmg(self, enemy):
        self.hp = self.hp - enemy
