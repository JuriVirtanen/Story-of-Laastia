import pygame
import os

class Tile:

    def __init__(self, x, y):
        self.ramka = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'frame.png')),(100, 100))
        self.image = None
        self.x = x
        self.y = y
        self.pixel_position = (((self.x-1)*100+5), ((self.y-1)*100+5))
        self.character = None