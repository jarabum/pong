import pygame
from random import randint

import velikostokna
from palka import Palka
from micek import Micek

pygame.init()

oknosirka = velikostokna.oknosirka
oknovyska = velikostokna.oknovyska

okno = pygame.display.set_mode((oknosirka, oknovyska))
okno.fill((0, 0, 0))
pygame.display.set_caption("pong")

palka1 = Palka(okno, 50, 0)
palka2 = Palka(okno, oknosirka - 100, 1)

micek = Micek(okno, oknosirka / 2 - 25, oknovyska / 2 - 25, palka1, palka2)

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    okno.fill((0, 0, 0))

    palka1.update()
    palka2.update()
    micek.update()

    palka1.display()
    palka2.display()
    micek.display()

    pygame.display.update()
