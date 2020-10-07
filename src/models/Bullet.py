import pygame
import os


IMAGE = "carrot.png"
BULLET_SCALE = (50, 40)
VELOCITY = 5


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(os.path.join("assets", IMAGE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += VELOCITY
