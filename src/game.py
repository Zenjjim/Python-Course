
import pygame
import random
from CrackHead import CrackHead
from BugBunny import BugBunny
from Bullet import Bullet

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
CRACKHEAD_COUNT = 15
HIT_DAMAGE = 5

score = 0

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Carrot the Crackhead')
font = pygame.font.Font(None, 36)

bullet_list = pygame.sprite.Group()
crackhead_list = pygame.sprite.Group()

bug_bunny_sprite = pygame.sprite.Group()
bug_bunny = BugBunny(50, SCREEN_HEIGHT/2)
bug_bunny_sprite.add(bug_bunny)

list_of_sprites = [crackhead_list, bullet_list, bug_bunny_sprite]

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

    # Wave crackheads
    if len(crackhead_list) == 0:
        for i in range(random.randrange(CRACKHEAD_COUNT)):
            crackhead_list.add(CrackHead())

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


    # Bullet
    for bullet in bullet_list:
        crackhead_hit_list = pygame.sprite.spritecollide(
            bullet, crackhead_list, False)
        if crackhead_hit_list:
            crackhead_list.remove(crackhead_hit_list[0])
            bullet_list.remove(bullet)
            score += 1
        if bullet.rect.x > SCREEN_WIDTH:
            bullet_list.remove(bullet)

    # Crack
    for crackhead in crackhead_list:
        if crackhead.rect.x < 0:
            crackhead_list.remove(crackhead)
            bug_bunny.health -= HIT_DAMAGE

    # Player hit Crackhead
    if pygame.sprite.spritecollide(bug_bunny, crackhead_list, True):
        bug_bunny.health -= HIT_DAMAGE

    for sprite in list_of_sprites:
        sprite.update()
        sprite.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
