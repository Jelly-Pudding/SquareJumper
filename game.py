import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500))
the_square = pygame.Rect(10, 240, 10, 10)
pygame.display.set_caption("Square Jumper")

def displayer():
    pygame.draw.rect(screen, (0, 255, 0), the_square)
    pygame.display.update()

running = True

while running == True:
    displayer()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
