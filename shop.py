import pygame
from gameOverScreen import importFont
from background import screen

dmgPrice =3
speedPrice =3
healthPrice =2
#shop is active make button presses relate to buying upgrades
def buyDmg(p):
    global dmgPrice
    if p.money>=dmgPrice:
        p.money=p.money-dmgPrice
        p.dmg = p.dmg+1
        dmgPrice=dmgPrice*2
def buySpeed(p):
    global speedPrice
    if p.money>=speedPrice:
        p.money=p.money-speedPrice
        p.move_speed = p.move_speed+2
        speedPrice=speedPrice*2
def buyHp(p):
    global healthPrice
    if p.money>=healthPrice:
        p.money=p.money-healthPrice
        p.heal(1)
        healthPrice=healthPrice+1
def merchartFirsttime(current_level):
   if current_level==1:
    font= importFont(40)
    text= font.render("The merchant appear from his hiding spot and tells you about the power, speed and health you can have if you pay him of course",False,(200,0,0))    
    screen.blit(text,(100,1050))
      

def drawInstruction(current_level,p):

    font= importFont(40)
    text= font.render("Please kill all the enemies with your sword attack by press spacebar",False,(200,0,0))    
    screen.blit(text,(100,1000))
    
    if current_level>=2 and p.hp>0:
     text= font.render("But little to no suprise that he runs away when danger arises",False,(200,0,0))
     screen.blit(text,(100,1050))

def resetPrice():
  global dmgPrice
  global speedPrice
  global healthPrice
  dmgPrice=3
  speedPrice=3
  healthPrice=2

def drawPrice(p):
 font = importFont(40)  
 if p.hp>0:
     dmgStat= font.render("B to increase Damage $"+str(dmgPrice),False,(200,0,0))
     screen.blit(dmgStat,(100,1100))
     dmgStat= font.render("N to increase Movement speed $"+str(speedPrice),False,(200,0,0))
     screen.blit(dmgStat,(100,1150))
     dmgStat= font.render("M to increase Health $"+str(healthPrice),False,(200,0,0))
     screen.blit(dmgStat,(100,1200))
       

def drawstat(p):
 global dmpPrice
 font = importFont(24)  
 dmgStat= font.render("Damage:"+str(p.dmg)+" Upgrade (B):"+str(dmgPrice),False,(200,0,0))
 screen.blit(dmgStat,(1700,0))
 dmgStat= font.render("Speed:"+str(p.move_speed)+" Upgrade (N):"+str(speedPrice),False,(200,0,0))
 screen.blit(dmgStat,(1700,40))
 dmgStat= font.render("Health:"+str(p.hp)+" add heart (M):"+str(healthPrice),False,(200,0,0))
 screen.blit(dmgStat,(1700,80))
 
 


