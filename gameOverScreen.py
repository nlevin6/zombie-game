import pygame,time,sys
from pygame import mixer

def importFont(size):
   return pygame.font.SysFont("EightBitDragon-anqx.ttf",size)


from background import screen

def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(2)

def GameOverScreen(player,level):
 mixer.music.load('ending.mp3')
 mixer.music.play(-1)
 stillPlaying =True
 font = importFont(50)
 font1 = importFont(40)

 fade(1920,1080)
 gameOverText=font.render("Gameover at level:" + str(level), False,(0,200,0))
 screen.blit(gameOverText,(1920/2-300,1080/2-100))
 gameOverText1=font1.render("e to restart, q to quit", False,(0,200,0))
 screen.blit(gameOverText1,(1920/2-300,1080/2))
 
 pygame.display.update()

# this "freezes" the 
 while(stillPlaying):
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e:
             mixer.music.load('campfire.mp3')
             mixer.music.play(-1)
             stillPlaying=False  
             player.hp=4
             #reset postion
             level=0
             #something magical to restart the game

        if event.key== pygame.K_q or event.key == pygame.K_ESCAPE:
              pygame.quit()
              sys.exit()
               

