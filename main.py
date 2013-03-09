import pygame, sys
from pygame.locals import *
pygame.init()
#width = 800
#height = 600
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN,32)
width, height = screen.get_size()
font = pygame.font.SysFont("monospace", 36)

background = pygame.image.load("bg.jpg").convert()
ball = pygame.image.load("ball.png").convert_alpha()
playerBar = pygame.image.load("Player_bar.png").convert_alpha()
botBar = pygame.image.load("Bot_bar.png").convert_alpha()
moveBallX = 1
moveBallY = 1
ballWidth = ball.get_width()
ballHeight = ball.get_height()
ballX = width/2 - ballWidth/2
ballY = height/2 - ballHeight/2
botWidth = 200
botHeight = 15
botX = width / 2 - botWidth / 2
botY = 0
scoreBot = 0
scorePlayer = 0
playerX = 0

def moveBall():
    global ball, ballX, ballY, moveBallX, moveBallY, ballHeight, ballWidth, scorePlayer, scoreBot, x, playerX
    if ballY == 20 and ballX >= botX and ballX <= botX + 200:
        ballY += 2
        moveBallY *= -1
    elif ballY == 0:
        scorePlayer += 1
        moveBallY *= -1
        ballY += 1
    if ballY == height - ballHeight and ballX >= playerX - 100 and ballX <= playerX + 100:
        moveBallY *= -1
    elif ballY == height - ballHeight:
        scoreBot += 1
        moveBallY *= -1
        ballY -= 1
    if ballX < 0 or ballX > width - ballWidth:
        moveBallX *= -1
    if ballY < 0 or ballY > height - ballHeight-1:
        moveBallY *= -1
    ballX += moveBallX
    ballY += moveBallY
def moveBot():
    global botX, botY, ballX, ballY, botWidth
    if botX < width - botWidth:
        if botX < ballX:
           botX += 1;
    if botX > ballX:
        botX -= 1;
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        '''if event.type == KEYDOWN:
            if event.key == K_LEFT:
                c -= 1
            elif event.key == K_RIGHT:
                c += 1
            elif event.key == K_UP:
                v -= 1
            elif event.key == K_DOWN:
                v += 1
        if event.type == KEYUP:
            if event.key == K_LEFT:
                c = 0
            elif event.key == K_RIGHT:
                c = 0
            elif event.key == K_UP:
                v = 0
            elif event.key == K_DOWN:
                v = 0'''
    moveBall()
    moveBot()
    #screen.blit(background, (0,0))
    screen.lock()
    pygame.draw.rect(screen, (0,145,175), (0,0,width,height), 0)
    screen.unlock()
    
    screen.blit(ball, (ballX,ballY))
    
    pygame.mouse.set_visible(False)
    
    x,y = pygame.mouse.get_pos()
    if x < 85:
        x = 85;
    if x > width - 115:
        x = width - 115;

    textPlayer = font.render(str(scorePlayer), 1, (255,55,0))
    textBot = font.render(str(scoreBot), 1, (255,55,0))
    screen.blit(textPlayer,(width - 100,height - 120))
    screen.blit(textBot,(width - 100,80))
    
    #screen.blit(ball, (x,y))
    screen.blit(playerBar, (x-85, height -15))
    screen.blit(botBar, (botX, botY))
    #screen.lock()
    #pygame.draw.rect(screen, (255,0,0), (botX, botY, botWidth, botHeight), 0)
    #pygame.draw.rect(screen, (255,0,0), (x - 85, height-10, 200,10),0)
    pygame.display.update()
    #screen.unlock()

    playerX = x
