import pygame
import os

pygame.init()
win = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Story of Laastia")

kratka = pygame.image.load("frame.png")
kratkalo = pygame.transform.scale(kratka, (100, 100))

def draw():
    win.blit(kratkalo, (0, 0))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
    pygame.quit()

if __name__ == "__main__":
    main()