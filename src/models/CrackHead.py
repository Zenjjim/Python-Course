import pygame
import random
import os
import constants

CRACKHEAD_IMAGES = ["crack_head_1.png",  "crack_head_2.png", "crack_head_3.png"]
CRACKHEAD_VELOCITY = 3

class CrackHead(pygame.sprite.Sprite):

    def __init__(self):
        CRACKHEAD_IMAGE = os.path.join("assets", random.choice(CRACKHEAD_IMAGES))
        super().__init__()

        self.image = pygame.image.load(CRACKHEAD_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = constants.SCREEN_WIDTH
        self.rect.y = max(0, min(constants.SCREEN_HEIGHT-self.rect.h,
                                 random.randint(0, constants.SCREEN_HEIGHT)))

    def update(self):
        self.rect.x -= CRACKHEAD_VELOCITY
