import pygame
import os

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

IMAGE = "bug_bunny.png"
START_HEALTH = 100

MOVE = 6


class BugBunny(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(os.path.join("assets", IMAGE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change = {"x": 0, "y": 0}
        self.health = START_HEALTH

