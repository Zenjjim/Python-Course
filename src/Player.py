import pygame
import os

SCREEN_WIDTH =  900
SCREEN_HEIGHT = 600

IMAGE = os.path.join("assets", "dude.png")
START_HEALTH = 100


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change = {"x": 0, "y": 0}
        self.health = START_HEALTH
        print(self.rect)
    def move(self, x, y):
        self.change["x"] += x
        self.change["y"] += y

    def update(self):
        self.rect.x = max(40, min(SCREEN_WIDTH-self.rect.w, self.rect.x + self.change["x"]))
        self.rect.y = max(0, min(SCREEN_HEIGHT-self.rect.h, self.rect.y + self.change["y"]))

        
