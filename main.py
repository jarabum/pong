import pygame
from random import randint

import windowsize
from paddle import Paddle
from ball import Ball

pygame.init()

windowwidth = windowsize.windowwidth
windowheight = windowsize.windowheight

window = pygame.display.set_mode((windowwidth, windowheight))
window.fill((0, 0, 0))
pygame.display.set_caption("pong")

paddle1 = Paddle(window, 50, 0)
paddle2 = Paddle(window, windowwidth - 100, 1)

ball = Ball(window, windowwidth / 2 - 25, windowheight / 2 - 25, paddle1, paddle2)

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill((0, 0, 0))

    paddle1.update()
    paddle2.update()
    ball.update()

    paddle1.display()
    paddle2.display()
    ball.display()

    pygame.display.update()
