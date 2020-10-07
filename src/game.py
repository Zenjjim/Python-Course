
import pygame
import random
from models import BugBunny

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
HIT_DAMAGE = 5

score = 0

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Carrot the Crackhead')
font = pygame.font.Font(None, 36)


bug_bunny_sprite = pygame.sprite.Group()
bug_bunny = BugBunny(50, SCREEN_HEIGHT/2)
bug_bunny_sprite.add(bug_bunny)

list_of_sprites = [bug_bunny_sprite]

clock = pygame.time.Clock()
done = False

while not done:
    # Exit if health is below 0
    if bug_bunny.health <= 0:
        done = True

    # Set  background color and list out score and health
    screen.fill((0, 0, 0))
    text = font.render(
        f"Health: {round(bug_bunny.health)}, Score: {score}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_x = 1
    text_y = 1
    screen.blit(text, [text_x, text_y])

    for sprite in list_of_sprites:
        sprite.update()
        sprite.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
