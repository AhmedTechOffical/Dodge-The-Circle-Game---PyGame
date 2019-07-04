import random
import pygame
import time
import sys
import math

pygame.init()


Position = [400,500]
pink= (249,4,188)
red = (244,66,66)
Blue = (66,98,244)
green = (0,255,0)
radius = 30
Black = (0,0,0)
color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

bg = pygame.image.load("bg.jpg")

font = pygame.font.SysFont('monospace',25)
font.set_bold(True)

pygame.display.set_caption('I actually Coded This!!')

screen_width = 800
screen_height = 600

velocity = 10
score = 0
timer = pygame.time.Clock()
paused = False

enemy_radius = 15
Position_E = [random.randint(0,screen_width-enemy_radius),enemy_radius]
eList = [Position_E]

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width,screen_height))

game_over = False
counting_time = pygame.time.get_ticks()
counting_seconds = str( (counting_time%60000)/1000 ).zfill(2)



def level(score,velocity):
    #if float(counting_seconds)>= 10:
     #   falling_enemies(eList)
      #  timer()
    if score <= 5000:
        velocity = 5
    if score > 5000:
        velocity = 7
    if score > 12500:
        velocity = 10
    if score > 25000:
        velocity = 12
    if score > 50000:
        velocity = 15
    if score > 100000:
        velocity = 20
    return velocity




def timer():
    counting_time = pygame.time.get_ticks()
    counting_seconds = str( (counting_time%60000)/1000 ).zfill(2)
    if not paused:

        counting_string = 'Time:' + (counting_seconds)
        counting_time = pygame.time.get_ticks() 
        counting_seconds = str( (counting_time%60000)/1000 ).zfill(2)
        counting_text = font.render(str(counting_string), 1, (pink))
        counting_rect = counting_text.get_rect(center = screen.get_rect().center)
    
    screen.fill((Black))
    screen.blit(counting_text, counting_rect)



def falling_enemies(eList,counting_seconds):
    lag = random.random()
    if len(eList) < 100000 and lag<0.075:
        x_pos = random.randint(0,screen_width-enemy_radius)
        y_pos = 0
        eList.append([x_pos,y_pos])
    if float(counting_seconds) >= 10.0:
        lag < 1.0
    

def draw_enemies(eList):
    for Position_E in eList:
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.draw.circle(screen,color,(Position_E[0],Position_E[1]),enemy_radius) # IF you get too dizzy wen seeing the enemy color, change color into red


def update_enemy_pos(eList,score):
    for  idx,Position_E in enumerate(eList):
        if Position_E[1] >= 0 and Position_E[1] < screen_height:
            Position_E[1] += velocity #Chaging Y position so its falling down, Velocity is just how fast Y coord is changing
        elif Position_E[1] <= 0 or Position_E[1] <= screen_height:
         #   eList.pop()
        #else:
            
            score+=1  
    return score         


      


    #else:
    # Position_E[1] = 0
     #   Position_E[0] = random.randint(0,screen_width-enemy_radius)

    #if collsion(Position,Position_E):
     #   game_over = True #or sys.exit() -- Wen its game over screen shuts down - FIX THIS!

def collision(Position,Position_E):
    x = Position[0]
    y = Position[1]

    ex = Position_E[0]
    ey = Position_E[1]

    if (ex >= x and ex < (x + radius)) or (x >= ex and x < (ex + enemy_radius)):
        if (ey >= y and ey < (y + radius)) or (y >= ey and y < (ey + enemy_radius)):
            return True

    else:
        return False

def collision_check(eList,Position):
    for Position_E in eList:
        if collision(Position_E,Position):
            return True 
    return False



while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                
                Position[0] -= radius

            if event.key == pygame.K_RIGHT:
                
                Position[0] += radius

            Position = [Position[0],Position[1]]
     #Position of enemy changing 
    screen.blit(bg,[0,0])
    if Position_E[1] >= 0 and Position_E[1] < screen_height:
        Position_E[1] += velocity #Chaging Y position so its falling down, Velocity is just how fast Y coord is changing 

    else:
        Position_E[1] = 0
        Position_E[0] = random.randint(0,screen_width-enemy_radius)

    
    
    
    timer()
    falling_enemies(eList,counting_seconds)
    screen.blit(bg,[0,0])
    score = update_enemy_pos(eList,score)
    
    velocity = level(score,velocity)
    
    text = 'Score:' + str(score)
    label = font.render(text,1,green)
    
    screen.blit(label,(screen_width-800,screen_height-150))
    

    draw_enemies(eList)

    if collision_check(eList,Position):
        game_over = True
    



    
    
    pygame.draw.circle(screen,green,(Position[0],Position[1]),radius)

    clock.tick(30)




    pygame.display.update()

