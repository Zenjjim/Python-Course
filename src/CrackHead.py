import pygame
import random
import os

IMAGES = ["crack_head_1.png",  "crack_head_2.png", "crack_head_3.png"]
CRACKHEAD_IMAGE = pygame.image.load(random.choice(IMAGES))
VELOCITY = 3

class CrackHead(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(CRACKHEAD_IMAGE)
        self.rect = self.image.get_rect() 

    def update(self):
        self.rect.x -= VELOCITY