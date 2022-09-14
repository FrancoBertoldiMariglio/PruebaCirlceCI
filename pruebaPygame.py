from re import T
import pygame
from pygame.locals import *
import random

blueP = (20, 34, 238)
greenP = (20, 240, 50)
redP = (230, 0, 20)
BLACK = (0, 0, 0)
sizeSquare = 75
""" px = int(eval("emptyColumn"))
py = int(eval(input("Column")))

x = 0
y = 0
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
gameOver = False

while "self.game.winCondition == False":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill(BLACK)
    Tx = 0
    Ty = 0
    for i in range(1, size[0], 40):
        for j in range(1, size[1], 40):
            pygame.draw.rect(screen, blueP, [i, j, 38, 38], 0)
            if py == 0:
                y = 1
            elif py == Ty:
                y = j
            Ty += 1
        if px == 0:
            x = 1
        elif px == Tx:
            x = i
        Tx += 1
        Ty = 0
    colAl = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
    pygame.draw.rect(screen, colAl, [x, y, 38, 38], 0)
    pygame.display.flip()
    clock.tick(5)
pygame.quit() """

pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
screen.fill(BLACK)
while True:
    pygame.draw.rect(screen, BLACK, (200, 150, 100, 50))