"""t3.py"""
import pygame
import sys

screen = pygame.display.set_mode((640, 480))
player = pygame.image.load('ball.bmp').convert()
background = pygame.image.load('bg1600x1200.jpg').convert()
screen.blit(background, (0, 0))
objects = []

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(self.speed, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0
        if self.pos.bottom > 400:
            self.pos.top = 0

for x in range(10):                    #create 10 objects</i>
    o = GameObject(player, x*40, x)
    objects.append(o)
while 1:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    #pygame.time.delay(1)
