import pygame
import random
import os

SCREEN_WIDTH =  900
SCREEN_HEIGHT = 600

IMAGES = ["crack_head_1.png",  "crack_head_2.png", "crack_head_3.png"]
VELOCITY = 3

class CrackHead(pygame.sprite.Sprite):

    def __init__(self):
        CRACKHEAD_IMAGE =  os.path.join("assets", random.choice(IMAGES))
        super().__init__()

        self.image = pygame.image.load(CRACKHEAD_IMAGE)
        self.rect = self.image.get_rect() 
        self.rect.x = SCREEN_WIDTH
        self.rect.y =  max(0, min(SCREEN_HEIGHT-self.rect.h, random.randint(0,SCREEN_HEIGHT)))

    def update(self):
        self.rect.x -= VELOCITY