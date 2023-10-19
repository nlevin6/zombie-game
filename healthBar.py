
import pygame
#get the screen
from background import screen
from gameOverScreen import importFont 
#images of hearts not swords 
HeartImg= pygame.image.load('door/pixelHeart-.png').convert_alpha()
playerHeartImg = pygame.transform.scale(HeartImg, (50, 50))
enemyHeartImg= pygame.transform.scale(HeartImg, (25,25 ))
# this draws the player hp bar 
def drawHpBar(p):
   
 i=0
 #prints player hearts
 while i<p.hp:
  screen.blit(playerHeartImg,(100+i*50,100))
  i=i+1
#this draws the hp of the enemy
#e= enemy object
def drawEnemyHpBar(e):
 #Prints the hp of the e(enemy) as a number 
 #font = importFont(0)
 #enemyHpBar= font.render("hp:"+str(e.hp),False,(200,0,0))
 #screen.blit(enemyHpBar,(e.get_enemy_x()-10,e.get_enemy_y()))
 
 #Draws the hearts over the e(enemy) head 
 i=0
 while i<e.hp:
  screen.blit(enemyHeartImg,(e.get_enemy_x()+i*35,e.get_enemy_y()-20))
  i=i+1


def drawBossHpBar(e):
 # Prints the hp of the e(enemy) as a number
 # font = importFont(0)
 # enemyHpBar= font.render("hp:"+str(e.hp),False,(200,0,0))
 # screen.blit(enemyHpBar,(e.get_enemy_x()-10,e.get_enemy_y()))

 # Draws the hearts over the e(enemy) head
 i = 0
 while i < e.hp:
  screen.blit(enemyHeartImg, (e.get_boss_x() + i * 35, e.get_boss_y() - 20))
  i = i + 1
    