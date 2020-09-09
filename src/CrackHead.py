import pygame
import random
import os

crackHeads = []
crackHeads.append(pygame.image.load(os.path.join("assets", "crack_head_2.png")))
crackHeads.append(pygame.image.load(os.path.join("assets", "crack_head_1.png")))
crackHeads.append(pygame.image.load(os.path.join("assets", "crack_head_3.png")))

class CrackHead(pygame.sprite.Sprite):

    def __init__(self):
    
        super().__init__()

        self.image = crackHeads[random.randrange(len(crackHeads))]
        self.rect = self.image.get_rect() 

    def update(self):
        self.rect.x -= 3