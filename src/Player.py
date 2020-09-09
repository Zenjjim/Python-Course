import pygame
from Color import BLACK
import os

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):

  
        super().__init__()
 

        self.image = pygame.image.load(os.path.join("assets", "dude.png"))
        self.health = 100
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
 
       
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):

        self.change_x += x
        self.change_y += y
 
    def update(self): 
        self.rect.x += self.change_x
        self.rect.y += self.change_y
