import pygame
import os
from Color import BLACK

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load(os.path.join("assets", "carrot.png"))
        self.image = pygame.transform.scale(self.image, (50,40))
        
 
        self.rect = self.image.get_rect()
 
    def update(self):
    
        self.rect.x += 5
