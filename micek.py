import pygame
import velikostokna
from random import randint

oknovyska = velikostokna.oknovyska
oknosirka = velikostokna.oknosirka

class Micek:
    def __init__(self, okno, x, y, palka1, palka2):
        self.okno = okno
        self.x = x
        self.y = y
        self.vyska = 50
        self.sirka = 50
        self.barva = (255, 255, 255)
        self.vx = randint(2, 4)
        self.vy = randint(1, 5)
        self.zrychleni = 0.3
        self.palka1 = palka1
        self.palka2 = palka2
        self.rect = pygame.Rect(self.x, self.y, self.sirka, self.vyska)
        self.palka1kolize = False
        self.palka2kolize = False
    def display(self):
        pygame.draw.rect(self.okno, self.barva, [self.x, self.y, self.sirka, self.vyska])
    def update(self):
        kolize1 = self.rect.colliderect(self.palka1.rect)
        kolize2 = self.rect.colliderect(self.palka2.rect)

        if self.y >= oknovyska - self.vyska or self.y <= 0:
            self.vy *= -1

        if kolize1 and not self.palka1kolize:
            self.vx *= -1
            self.vx += self.zrychleni
            if self.vy < 0:
                self.vy -= self.zrychleni
            else:
                self.vy += self.zrychleni
            self.palka1kolize = True
            self.palka2kolize = False

        if kolize2 and not self.palka2kolize:
            self.vx *= -1
            self.vx -= self.zrychleni
            if self.vy < 0:
                self.vy -= self.zrychleni
            else:
                self.vy += self.zrychleni
            self.palka1kolize = False
            self.palka2kolize = True

        if self.x <= 0 or self.x >= oknosirka + self.sirka:
            self.smrt()

        self.x += self.vx
        self.y += self.vy
        self.rect.topleft = (self.x, self.y)
    def smrt(self):
        self.vx = 0
        self.vy = 0
        self.x = oknosirka / 2 - self.sirka / 2
        self.y = oknovyska / 2 - self.vyska / 2
        self.display()
        pygame.time.delay(500)
        self.vx = randint(2, 4)
        self.vy = randint(1, 5)
