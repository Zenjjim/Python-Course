
import pygame
import random
from models import BugBunny, Bullet
import constants

score = 0

pygame.init()

screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])
pygame.display.set_caption('Carrot the Crackhead')
font = pygame.font.Font(None, 36)

bullet_list = pygame.sprite.Group()

bug_bunny_sprite = pygame.sprite.Group()
bug_bunny = BugBunny(50, constants.SCREEN_HEIGHT/2)
bug_bunny_sprite.add(bug_bunny)

list_of_sprites = [bullet_list, bug_bunny_sprite]


clock = pygame.time.Clock()
done = False

while not done:

    # Set  background color and list out score and health
    screen.fill((0, 0, 0))
    text = font.render(
        f"Health: {round(bug_bunny.health)}, Score: {score}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_x = 1
    text_y = 1
    screen.blit(text, [text_x, text_y])

    # Key input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        bug_bunny.move(event, pygame)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = bug_bunny.rect.x + bug_bunny.image.get_width()
                bullet_y = bug_bunny.rect.y + bug_bunny.image.get_height()/2
                bullet_list.add(Bullet(bullet_x, bullet_y))

    for sprite in list_of_sprites:
        sprite.update()
        sprite.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
