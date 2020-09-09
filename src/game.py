
import pygame
import random
from Block import Block
from Player import Player
from Bullet import Bullet
from Color import BLACK,BLUE,RED,WHITE
import os


pygame.init()
 
screen_width =  900
screen_height = 600

score = 0
move = 6

crackHeads = []
crackHeads.append(pygame.image.load(os.path.join("assets", "crack_head_2.png")))
crackHeads.append(pygame.image.load(os.path.join("assets", "crack_head_1.png")))
crackHeads.append(pygame.image.load(os.path.join("assets", "crack_head_3.png")))

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Test')
font = pygame.font.Font(None, 36)
 
bullet_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

player = Player(50, 50)
all_sprites_list.add(player)
player.rect.y = 370
    
 
def create_blocks():
    for i in range(random.randrange(15)):
           
        block = Block(BLUE, crackHeads)
 

        block.rect.x = screen_width
        block.rect.y = random.randrange(screen_height)
 

        block_list.add(block)
        all_sprites_list.add(block)

 
clock = pygame.time.Clock()
done = False
 
while not done:
    if player.health <= 0:
            done = True
            
    if len(block_list) == 0:
        create_blocks()
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.changespeed(-move, 0)
            elif event.key == pygame.K_d:
                player.changespeed(move, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, -move)
            elif event.key == pygame.K_s:
                player.changespeed(0, move)
 

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed(move, 0)
            elif event.key == pygame.K_d:
                player.changespeed(-move, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, move)
            elif event.key == pygame.K_s:
                player.changespeed(0, -move)
        elif event.type == pygame.MOUSEBUTTONDOWN:
        
            bullet = Bullet()
            bullet.rect.x = player.rect.x + player.image.get_width()
            bullet.rect.y = player.rect.y + player.image.get_height()/2
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
 
 
    all_sprites_list.update()
    
    if pygame.sprite.spritecollide(player, block_list,True):
        player.health -= 25

   
    for bullet in bullet_list:
 
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
      
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
 
     
        if bullet.rect.x > screen_width:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
 
    for block in block_list:
        if block.rect.x < 0:
            block_list.remove(block)
            all_sprites_list.remove(block)
            player.health -= 10


    screen.fill(WHITE)
    text = font.render(f"lives: {player.health}", True, BLACK)
    text_rect = text.get_rect()
    text_x = 1
    text_y = 1
    screen.blit(text, [text_x, text_y])

    all_sprites_list.draw(screen)
 
  
    pygame.display.flip()
 

    clock.tick(60)
 
pygame.quit()
