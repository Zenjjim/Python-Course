import pygame
import os
import constants

BULLET_IMAGE = "carrot.png"
BULLET_VELOCITY = 5

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(os.path.join("assets", BULLET_IMAGE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += BULLET_VELOCITY
