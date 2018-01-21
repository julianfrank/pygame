"""t2"""
import sys
import pygame

pygame.init()

print("starting ...")
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

background = pygame.image.load("bg1600x1200.jpg").convert()
screen.blit(background, (0, 0))

ball = pygame.image.load("ball.bmp").convert()
ballpos = ball.get_rect()
screen.blit(ball, ballpos)

pygame.display.update()

for x in range(100):
    screen.blit(background, ballpos, ballpos)
    ballpos = ballpos.move(1, 1)
    screen.blit(ball, ballpos)
    pygame.display.update()
    pygame.time.delay(10)
    print(x)

while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
