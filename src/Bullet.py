import pygame
from Color import BLACK

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self):

        super().__init__()

        self.image = pygame.Surface([10, 4])
        # self.image = pygame.transform.rotate(self.image, -90)
        self.image.fill(BLACK)
        
 
        self.rect = self.image.get_rect()
 
    def update(self):
    
        self.rect.x += 3
