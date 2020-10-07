import pygame
import os

IMAGE = "definitely_not_weed.png"


class DefinitelyNotWeed(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.image.load(os.path.join("assets", IMAGE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.h/2
