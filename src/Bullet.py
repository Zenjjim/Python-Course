import pygame
import os


IMAGE = os.path.join("assets", "carrot.png")
BULLET_SCALE = (50, 40)
VELOCITY = 5

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += VELOCITY
