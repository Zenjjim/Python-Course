import pygame
import random
import os
ships = []
ships.append(pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png")))
ships.append(pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png")))
ships.append(pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png")))

class Block(pygame.sprite.Sprite):

    def __init__(self, color):

        super().__init__()

        self.image = ships[random.randrange(len(ships))]
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect() 

    def update(self):
        self.rect.x -= 3