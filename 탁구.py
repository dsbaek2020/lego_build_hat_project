'''
from buildhat import Motor
from signal import pause
motor_left = Motor('A')

def moved_left(motor_speed, motor_pos, motor_apos):
    print(morot_apos)
    
motor_left.when_rotated = moved_left
pause()

while True:
    print (motor_left.get_aposition())
    
    
    
'''

import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
from time import sleep
from buildhat import Motor

windowsWidth = 640
windowsHeight = 480

#---motor (joystick ) -------------------------
#paddle position
pos_left = int(windowsHeight/2)
pos_right = int(windowsHeight/2)
Tenshouin = int(windowsHeight/2)


#ball postion, speed
ballX = int(windowsWidth/2)
ballY = int(windowsHeight/2)
ball_Vx = 4.0
ball_Vy = -4.0


def handle_motor(speed, pos, apos):
    print("Motor", speed, pos, apos)


def moved_left(motor_speed, motor_rpos, motor_apos):
    global pos_left
    pos_left = pos_left + (motor_speed*2.0)
    
    #print("Motor", motor_speed, motor_rpos, motor_apos)
    #motor_left.when_rotated = moved_left
    
def moved_right(motor_speed, motor_rpos, motor_apos):
    global pos_right
    pos_right = pos_right + (motor_speed*2.0)
    
    
    

motor_left = Motor('A')
motor_left.when_rotated = moved_left

motor_right = Motor('D')
motor_right.when_rotated = moved_right
#----------------------------------------------

#---screen, paddle ----------------------------

hexTable = {'0' : 0,
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            'a' : 10,
            'b' : 11,
            'c' : 12,
            'd' : 13,
            'e' : 14,
            'f' : 15}


def hex_to_tupleRGB(hexColor):
    r = hexTable[ hexColor[1] ]*16 + hexTable[ hexColor[2] ]
    g = hexTable[ hexColor[3] ]*16 + hexTable[ hexColor[4] ]
    b = hexTable[ hexColor[5] ]*16 + hexTable[ hexColor[6] ]

    return (r, g, b)

red = hex_to_tupleRGB("#d70035")
blue = (0, 6, 141)
lemon = hex_to_tupleRGB("#fff352")
Eichi = hex_to_tupleRGB("#fff3b8")
pink = hex_to_tupleRGB("#f5b2b2")

ball = {'radious' : 10,
         'color': lemon}


#define paddle class ------------------------------
class paddle(object):
    def __init__(self, surface, pos_x, pos_y,
                 width, height, color):
        
        self.surface = surface
        self.pos_x  = int(pos_x)
        self.pos_y  = int(pos_y)
        self.width  = int(width)
        self.height = int(height)
        self.color  = color
        
        
    def draw(self):
        pygame.draw.rect(self.surface, self.color,
                          ( self.pos_x, self.pos_y, self.width, self.height) )
        
    def setPaddlePosition_y(self, y):
        self.pos_y = int(y)
    
    def set_color(self, color):
         self.color  = color
#-------------------------------------------------        

pygame.init()

surface = pygame.display.set_mode((windowsWidth, windowsHeight))
pygame.display.set_caption('Ping Pong Game')




#define left paddle
leftPaddle =  paddle(surface, 40, pos_left, 20, 100, red)
rightPaddle = paddle(surface, 590, pos_right, 20, 100, blue)
brick = paddle(surface, 620, Tenshouin, 10, 50, Eichi)
time = 0


while True:
    surface.fill((0,0,0))
    
    #draw paddle
    
    rightPaddle.setPaddlePosition_y(pos_right)
    rightPaddle.draw()
    
    leftPaddle.setPaddlePosition_y(pos_left)
    leftPaddle.draw()
    
    brick.setPaddlePosition_y(Tenshouin)
    brick.draw()
    
    #draw ball 
    pygame.draw.circle(surface, ball['color'], (int(ballX), int(ballY)),  ball['radious'], 1)
    pygame.display.update()
    
    
    #move ball 
    ballX = ballX + ball_Vx
    ballY = ballY + ball_Vy
    
    #print('ball y position = ', ballY)
    
    if ballY > windowsHeight-10:  # on bottom, Vy = Vy * -1
        ball_Vy *= -1
        
    if ballY < 10:                # on top, Vy = Vy * -1  
        ball_Vy *= -1
    
    
    if ballX > windowsWidth-10:
        ball_Vx *= -1

    if ballX < 10:
        ball_Vx *= -1
        
    # When colliding ball with left paddle,
    #then ball's direction and horizontal speed Vx must inverse.      
    if ballX<50+30 and pos_left<ballY<(pos_left+100):
        ball_Vx *= -1
        
    if ballX>550+30 and pos_right<ballY<(pos_right+100):
        ball_Vx *= -1
        
    if ballX>580+30 and Tenshouin<ballY<(Tenshouin+100):
        ball_Vx *= -1
        brick.set_color(pink)
        time = 0
        

    sleep(0.01)
    time = time+0.01
    print('time=', time)
    
    if time > 5:
        brick.set_color(Eichi)
    
    #pygame.draw.rect(surface, blue, (100, int(pos_left), 10, 40) )
    