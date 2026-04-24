import pygame
import windowsize
from random import randint

windowwidth = windowsize.windowwidth
windowheight = windowsize.windowheight

class Ball:
    def __init__(self, window, x, y, paddle1, paddle2):
        self.window = window
        self.x = x
        self.y = y
        self.height = 50
        self.width = 50
        self.color = (255, 255, 255)
        self.vx = randint(2, 4)
        self.vy = randint(1, 5)
        self.vel = 0.3
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.paddle1collision = False
        self.paddle2collision = False
    def display(self):
        pygame.draw.rect(self.window, self.color, [self.x, self.y, self.width, self.height])
    def update(self):
        collision1 = self.rect.colliderect(self.paddle1.rect)
        collision2 = self.rect.colliderect(self.paddle2.rect)

        if self.y >= windowheight - self.height or self.y <= 0:
            self.vy *= -1

        if collision1 and not self.paddle1collision:
            self.vx *= -1
            self.vx += self.vel
            if self.vy < 0:
                self.vy -= self.vel
            else:
                self.vy += self.vel
            self.paddle1collision = True
            self.paddle2collision = False

        if collision2 and not self.paddle2collision:
            self.vx *= -1
            self.vx -= self.vel
            if self.vy < 0:
                self.vy -= self.vel
            else:
                self.vy += self.vel
            self.paddle1collision = False
            self.paddle2collision = True

        if self.x <= 0 or self.x >= windowwidth + self.width:
            self.death()

        self.x += self.vx
        self.y += self.vy
        self.rect.topleft = (self.x, self.y)
    def death(self):
        self.vx = 0
        self.vy = 0
        self.x = windowwidth / 2 - self.width / 2
        self.y = windowheight / 2 - self.height / 2
        self.rect.topleft = (self.x, self.y)
        self.display()
        pygame.time.delay(500)
        self.vx = randint(2, 4)
        self.vy = randint(1, 5)
