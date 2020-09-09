import pygame
import random


class Block(pygame.sprite.Sprite):

    def __init__(self, images):

        super().__init__()

        self.image = images[random.randrange(len(images))]
        self.rect = self.image.get_rect() 

    def update(self):
        self.rect.x -= 3