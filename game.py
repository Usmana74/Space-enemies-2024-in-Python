import pygame
import random
import math

pygame.init()    #initialization

screen=pygame.display.set_mode((800,600))                         #defining screen size

pygame.display.set_caption('Space Enemies 2024')                  #setting game name that appears on top

background = pygame.image.load('background.png')                  #Background image

photo= pygame.image.load('space-invaders.png')                    #settin logo
pygame.display.set_icon(photo)

playerimage= pygame.image.load('space-ship.png')                  #setting controller image that runs

playerX=400                                                       # to set image on screen
playerY=500
playerX_change = 0


enemyimage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies) :
   enemyimage.append (pygame.image.load('play.png'))                        #setting enemy image that runs
   enemyX.append (random.randint(0,735))                                     # to set image on screen
   enemyY.append (random.randint(50,150))
   enemyX_change .append ( 3)
   enemyY_change .append ( 40 )


bulletimage= pygame.image.load('bullet.png')                        #setting bullet image that runs
bulletX = 0                                                       # to set image on screen
bulletY = 500
bulletX_change = 0
bulletY_change = 10
bullet_state= "ready"                                             #ready to not show bullet on screen
                                                                  # fire: the bullet is currently moving

score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)

textX = 10
textY = 10

over_text = pygame.font.Font("freesansbold.ttf",64)


def game_over_text() :
     game_over = over_text.render("GAME OVER",True, (255,255,255))
     screen.blit(game_over, (200,256))

def show_score(x,y) :
    score = font.render("score :" + str(score_value),True, (255,255,255))
    screen.blit(score, (x,y))
    
def player(x,y) :
    screen.blit(playerimage, (x,y))


def enemy(x,y,i) :
    screen.blit(enemyimage[i], (x,y))

def fire_bullet(x,y) :
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimage,(x+16,y+10))
    
def isCollision(enemyX,enemyY,bulletX,bulletY) :
    distance =  math.sqrt(math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2)))  
    if distance <27 :
        return True
    else:
        return False

running= True 
while running:
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                playerX_change = -5
            if event.key == pygame.K_RIGHT:   
                playerX_change = 5
            if event.key == pygame.K_SPACE :
                if bullet_state == "ready" :
                   bulletX=playerX
                   fire_bullet(bulletX,bulletY)
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 playerX_change = 0
       
                 
                 
    playerX+=playerX_change 
    if playerX < 0:
        playerX=0
    elif playerX>736:
        playerX=736
        
    for i in range(num_of_enemies) :
        
        if enemyY[i] > 440 :
            for j in range(num_of_enemies) :
                enemyY[j] = 2000 
            game_over_text()
            break
            
        
        enemyX[i]+=enemyX_change[i]
        if enemyX[i] < 0:
          enemyX_change[i] = 3
          enemyY[i]+=enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]            
            
            
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY) 
        if collision :
           bulletY = 500
           bullet_state = "ready"
           score_value +=1
           enemyX[i]=random.randint(0,735)                                  
           enemyY[i]=random.randint(50,150)    
           enemyX_change[i] = -3
           enemyY[i]+=enemyY_change[i]
           
        enemy(enemyX[i],enemyY[i],i)
        
    if bulletY<0 :                                       # returning bullet to its original position when it hits 0 Y-coordinate and so that's how we can shoot multiple bullets
        bulletY = 500
        bullet_state = "ready"   
    
    if bullet_state == "fire" :                           #Bullet Movement
        fire_bullet(bulletX , bulletY)
        bulletY -= bulletY_change
    
    player(playerX,playerY)
    show_score(textX,textY)
    
    pygame.display.update()
     
