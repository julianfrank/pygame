"""t3.py"""

import sys

import pygame

SCREEN = pygame.display.set_mode((640, 480))
PLAYER = pygame.image.load('ball.bmp').convert()
BG = pygame.image.load('bg1600x1200.jpg').convert()
SCREEN.blit(BG, (0, 0))
OBJECTS = []


class GameObject:
    """GameObject"""

    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        """move"""
        self.pos = self.pos.move(self.speed, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0
        if self.pos.bottom > 400:
            self.pos.top = 0

for x in range(10):                    #create 10 OBJECTS</i>
    o = GameObject(PLAYER, x*40, x)
    OBJECTS.append(o)
while 1:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()
    for o in OBJECTS:
        SCREEN.blit(BG, o.pos, o.pos)
        o.move()
        SCREEN.blit(o.image, o.pos)
    pygame.display.update()
    #pygame.time.delay(1)
