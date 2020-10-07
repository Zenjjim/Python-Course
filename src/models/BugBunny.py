import pygame
import os
import constants


class BugBunny(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(os.path.join("assets", constants.BUNNY_IMAGE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change = {"x": 0, "y": 0}
        self.health = constants.START_HEALTH

    def move(self, event, pygame):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.change["x"] -= constants.BUNNY_MOVE
            elif event.key == pygame.K_d:
                self.change["x"] += constants.BUNNY_MOVE
            elif event.key == pygame.K_w:
                self.change["y"] -= constants.BUNNY_MOVE
            elif event.key == pygame.K_s:
                self.change["y"] += constants.BUNNY_MOVE

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.change["x"] += constants.BUNNY_MOVE
            elif event.key == pygame.K_d:
                self.change["x"] -= constants.BUNNY_MOVE
            elif event.key == pygame.K_w:
                self.change["y"] += constants.BUNNY_MOVE
            elif event.key == pygame.K_s:
                self.change["y"] -= constants.BUNNY_MOVE

    def update(self):
        self.rect.x = max(40, min(constants.SCREEN_WIDTH-self.rect.w,
                                  self.rect.x + self.change["x"]))
        self.rect.y = max(0, min(constants.SCREEN_HEIGHT-self.rect.h,
                                 self.rect.y + self.change["y"]))
