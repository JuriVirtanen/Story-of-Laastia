import pygame
import os
from mapa import *

pygame.init()
win = pygame.display.set_mode((950, 580))
pygame.display.set_caption("Story of Laastia")

background = pygame.image.load(os.path.join('Assets', 'background2.png'))
win.blit(background,(0,0))
pygame.display.update()
a = Battlefield()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        a.draw(win)
    pygame.quit()

if __name__ == "__main__":
    main()