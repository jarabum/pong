import pygame
import windowsize

windowheight = windowsize.windowheight

class Paddle:
    def __init__(self, window, x, id):
        self.window = window
        self.x = x
        self.y = 0
        self.width = 50
        self.height = 200
        self.color = (255, 255, 255)
        self.id = id
        self.vel = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.Font("ArchivoBlack-Regular.ttf", 70)
        self.score = 0
        self.scoretext = self.font.render(str(self.score), True, (255, 255, 255))
    def display(self):
        pygame.draw.rect(self.window, self.color, [self.x, self.y, self.width, self.height])
        if self.id == 0:
            self.window.blit(self.scoretext, (self.x + 150, 60))
        elif self.id == 1:
            self.window.blit(self.scoretext, (self.x - 150, 60))
    def update(self):
        keys = pygame.key.get_pressed()
        if self.id == 0:
            if keys[pygame.K_s] and self.y <= windowheight - self.height:
                self.y += self.vel
                self.rect.topleft = (self.x, self.y)
            elif keys[pygame.K_w] and self.y >= 0:
                self.y -= self.vel
                self.rect.topleft = (self.x, self.y)
        if self.id == 1:
            if keys[pygame.K_DOWN] and self.y <= windowheight - self.height:
                self.y += self.vel
                self.rect.topleft = (self.x, self.y)
            elif keys[pygame.K_UP] and self.y >= 0:
                self.y -= self.vel
                self.rect.topleft = (self.x, self.y)
