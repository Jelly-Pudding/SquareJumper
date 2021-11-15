import pygame
import sys
import random

random_list_of_y_coords = random.sample(range(0, 500, 20), 5)

pygame.init()
screen = pygame.display.set_mode((500, 500))
the_square = pygame.Rect(10, 240, 10, 10)
enemy_square_1 = pygame.Rect(490, random_list_of_y_coords[0], 10, 10)
enemy_square_2 = pygame.Rect(490, random_list_of_y_coords[1], 10, 10)
enemy_square_3 = pygame.Rect(490, random_list_of_y_coords[2], 10, 10)
enemy_square_4 = pygame.Rect(490, random_list_of_y_coords[3], 10, 10)
enemy_square_5 = pygame.Rect(490, random_list_of_y_coords[4], 10, 10)
pygame.display.set_caption("Square Mover")
clock = pygame.time.Clock()

def displayer():
    pygame.draw.rect(screen, (0, 255, 0), the_square)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_1)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_2)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_3)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_4)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_5)
    pygame.display.update()

running = True

count = 0

while running == True:
    clock.tick(10)
    displayer()
    screen.fill((0,0,0))
    enemy_square_1 = pygame.Rect.move(enemy_square_1, -5, 0)  
    enemy_square_2 = pygame.Rect.move(enemy_square_2, -5, 0)
    enemy_square_3 = pygame.Rect.move(enemy_square_3, -5, 0)
    enemy_square_4 = pygame.Rect.move(enemy_square_4, -5, 0)
    enemy_square_5 = pygame.Rect.move(enemy_square_5, -5, 0) 
    # If an enemy square hits our green square, the game ends
    if pygame.Rect.colliderect(the_square, enemy_square_1) == True or pygame.Rect.colliderect(the_square, enemy_square_2) == True or pygame.Rect.colliderect(the_square, enemy_square_3) == True or pygame.Rect.colliderect(the_square, enemy_square_4) == True or pygame.Rect.colliderect(the_square, enemy_square_5) == True:
        print("Game Over!")
        pygame.quit()
        sys.exit()
    if enemy_square_1[0] == -20:
        #red squares reache the other end of the screen, so they all get reset
        random_list_of_y_coords = random.sample(range(0, 500, 20), 5)
        enemy_square_1 = pygame.Rect(490, random_list_of_y_coords[0], 10, 10)
        enemy_square_2 = pygame.Rect(490, random_list_of_y_coords[1], 10, 10)
        enemy_square_3 = pygame.Rect(490, random_list_of_y_coords[2], 10, 10)
        enemy_square_4 = pygame.Rect(490, random_list_of_y_coords[3], 10, 10)
        enemy_square_5 = pygame.Rect(490, random_list_of_y_coords[4], 10, 10)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_w:
                #moves the square up
                the_square = pygame.Rect.move(the_square, 0, -5)
            if event.key == pygame.K_s:
                #moves the square down
                the_square = pygame.Rect.move(the_square, 0, 5)
