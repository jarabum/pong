import pygame
import velikostokna

vyskahry = velikostokna.oknovyska

class Palka:
    def __init__(self, okno, x, id):
        self.okno = okno
        self.x = x
        self.y = 0
        self.sirka = 50
        self.vyska = 200
        self.barva = (255, 255, 255)
        self.id = id
        self.vel = 10
        self.rect = pygame.Rect(self.x, self.y, self.sirka, self.vyska)
    def display(self):
        pygame.draw.rect(self.okno, self.barva, [self.x, self.y, self.sirka, self.vyska])
    def update(self):
        keys = pygame.key.get_pressed()
        if self.id == 0:
            if keys[pygame.K_s] and self.y <= vyskahry - self.vyska:
                self.y += self.vel
                self.rect.topleft = (self.x, self.y)
            elif keys[pygame.K_w] and self.y >= 0:
                self.y -= self.vel
                self.rect.topleft = (self.x, self.y)
        if self.id == 1:
            if keys[pygame.K_DOWN] and self.y <= vyskahry - self.vyska:
                self.y += self.vel
                self.rect.topleft = (self.x, self.y)
            elif keys[pygame.K_UP] and self.y >= 0:
                self.y -= self.vel
                self.rect.topleft = (self.x, self.y)
