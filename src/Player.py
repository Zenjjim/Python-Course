import pygame
import os

IMAGE = os.path.join("assets", "dude.png")
START_HEALTH = 100


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change = {x: 0, y: 0}

        self.health = START_HEALTH

    def move(self, x, y):
        self.change.x += x
        self.change.y += y

    def update(self):
        self.rect.x += self.change.x
        self.rect.y += self.change.y
