
import pygame
import random
from CrackHead import CrackHead
from Player import Player
from Bullet import Bullet
from DefinitelyNotWeed import DefinitelyNotWeed
import os


pygame.init()
 
SCREEN_WIDTH =  900
SCREEN_HEIGHT = 600

score = 0
MOVE = 6


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Test')
font = pygame.font.Font(None, 36)
 
bullet_list = pygame.sprite.Group()
crackhead_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
not_a_weed_sprites_list = pygame.sprite.Group()

player = Player(50, 50)
all_sprites_list.add(player)
player.rect.y = 370
    
 
def create_crackheads():
    for i in range(random.randrange(30)):
           
        crackhead = CrackHead()
 

        crackhead.rect.x = SCREEN_WIDTH
        crackhead.rect.y = random.randrange(SCREEN_HEIGHT)
 

        crackhead_list.add(crackhead)
        all_sprites_list.add(crackhead)

 
clock = pygame.time.Clock()
done = False
PLANT_COUNT = 5
for i in range(0,PLANT_COUNT):
    not_weed = DefinitelyNotWeed(0,SCREEN_HEIGHT/PLANT_COUNT*i)

    not_a_weed_sprites_list.add(not_weed)
    all_sprites_list.add(not_weed)




while not done:
    if player.health <= 0:
            done = True
            
    if len(crackhead_list) == 0:
        create_crackheads()
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move(-MOVE, 0)
            elif event.key == pygame.K_d:
                player.move(MOVE, 0)
            elif event.key == pygame.K_w:
                player.move(0, -MOVE)
            elif event.key == pygame.K_s:
                player.move(0, MOVE)
 

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.move(MOVE, 0)
            elif event.key == pygame.K_d:
                player.move(-MOVE, 0)
            elif event.key == pygame.K_w:
                player.move(0, MOVE)
            elif event.key == pygame.K_s:
                player.move(0, -MOVE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
        
            bullet = Bullet()
            bullet.rect.x = player.rect.x + player.image.get_width()
            bullet.rect.y = player.rect.y + player.image.get_height()/2
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
 
 
    all_sprites_list.update()
    
    if pygame.sprite.spritecollide(player, crackhead_list,True):
        player.health -= 25

    
    for plant in not_a_weed_sprites_list:

        plant_hit_list = pygame.sprite.spritecollide(plant, crackhead_list, True)
   
        if plant_hit_list:
            not_a_weed_sprites_list.remove(plant)
            all_sprites_list.remove(plant)
            player.health -= (100/PLANT_COUNT)

    for bullet in bullet_list:
 
        crackhead_hit_list = pygame.sprite.spritecollide(bullet, crackhead_list, True)
 
      
        for crackhead in crackhead_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
 
     
        if bullet.rect.x > SCREEN_WIDTH:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
 
    for crackhead in crackhead_list:
        if crackhead.rect.x < 0:
            crackhead_list.remove(crackhead)
            all_sprites_list.remove(crackhead)
            player.health -= 10


    screen.fill((0,0,0))
    text = font.render(f"lives: {player.health}", True, (255,255,255))
    text_rect = text.get_rect()
    text_x = 1
    text_y = 1
    screen.blit(text, [text_x, text_y])

    all_sprites_list.draw(screen)
 
  
    pygame.display.flip()
 

    clock.tick(60)
 
pygame.quit()
