import pygame
import sys
import random

random_x_number = random.randrange(10, 50, 10)
random_y_number = random.randrange(10, 50, 10)	
print(random_x_number)
print(random_y_number)

pygame.init()
screen = pygame.display.set_mode((500, 500))
the_square = pygame.Rect(10, 240, 10, 10)
enemy_square = pygame.Rect(490, 240, 10, 10)
pygame.display.set_caption("Square Mover")

def displayer():
    pygame.draw.rect(screen, (0, 255, 0), the_square)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square)
    pygame.display.update()

running = True

count = 0

while running == True:
    count += 1
    displayer()
    screen.fill((0,0,0))
    if count % 100 == 0:
        enemy_square = pygame.Rect.move(enemy_square, -5, 0)   
    if enemy_square == pygame.Rect(0, 240, 10, 10):
        #red square reaches the other end of the screen, so gets reset
        enemy_square = pygame.Rect(490, 240, 10, 10)
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
