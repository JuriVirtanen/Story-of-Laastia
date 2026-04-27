import pygame
from tile import *

class Battlefield:
    def __init__(self):
        self.entity = []
        self.mapa = []
        for a in range(1, 6):
            for b in range(1, 6):
                self.mapa.append(Tile(a, b))

    def add_character(self, character, x, y):
        self.entity.append([character, x, y])

    def turn(self):
        for a in self.entity:
            for b in self.mapa:
                if b.x == a.x and b.y == a.y:
                    b.character = a.character

    def draw(self, windows):
        for tile in self.mapa:
            windows.blit(tile.ramka, tile.pixel_position)
        pygame.display.update()