import pygame
import random
import os
import constants



class CrackHead(pygame.sprite.Sprite):

    def __init__(self):
        CRACKHEAD_IMAGE = os.path.join("assets", random.choice(constants.CRACKHEAD_IMAGES))
        super().__init__()

        self.image = pygame.image.load(CRACKHEAD_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = constants.SCREEN_WIDTH
        self.rect.y = max(0, min(constants.SCREEN_HEIGHT-self.rect.h,
                                 random.randint(0, constants.SCREEN_HEIGHT)))

    def update(self):
        self.rect.x -= constants.CRACKHEAD_VELOCITY
