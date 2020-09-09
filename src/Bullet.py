import pygame
import os


IMAGE = os.path.join("assets", "carrot.png")
BULLET_SCALE = (50, 40)
VELOCITY = 5

class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(IMAGE)
        self.image = pygame.transform.scale(self.image, BULLET_SCALE)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += VELOCITY
