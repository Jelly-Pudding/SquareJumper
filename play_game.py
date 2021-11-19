# You can move faster in this version of the game (to help make it easier)
# Starts slow but the enemy's bullets speed up

from train import * 

laser_sound = pygame.mixer.Sound("gun_sound_effect.mp3")

def display():
    pygame.draw.rect(screen, (0, 255, 0), the_square)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_1)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_2)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_3)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_4)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_5)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_6)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_7)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_8)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_9)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_10)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_11)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_12)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square_13)
    pygame.draw.rect(screen, (255,165,0), shooty_square_1)
    pygame.draw.rect(screen, (255,165,0), shooty_square_2)
    pygame.draw.rect(screen, (255,165,0), shooty_square_3)
    pygame.draw.rect(screen, (255,165,0), shooty_square_4)
    pygame.draw.rect(screen, (255,165,0), shooty_square_5)
    pygame.draw.rect(screen, (255,165,0), shooty_square_6)
    pygame.draw.rect(screen, (255,165,0), shooty_square_7)
    pygame.draw.rect(screen, (255,165,0), shooty_square_8)
    pygame.draw.rect(screen, (255,165,0), shooty_square_9)
    pygame.draw.rect(screen, (255,165,0), shooty_square_10)
    pygame.draw.rect(screen, (255,165,0), shooty_square_11)
    pygame.draw.rect(screen, (255,165,0), shooty_square_12)
    pygame.draw.rect(screen, (255,165,0), shooty_square_13)
    pygame.display.update()

running = True
sound_for_first_shot = True
increase_speed = 0
while running:
    if sound_for_first_shot == True:
        pygame.mixer.Sound.play(laser_sound)
        sound_for_first_shot = False
    clock.tick(50 + increase_speed)        
    screen.fill((0,0,0))
    display()
    enemy_square_1 = pygame.Rect.move(enemy_square_1, -5, 0)  
    enemy_square_2 = pygame.Rect.move(enemy_square_2, -5, 0)
    enemy_square_3 = pygame.Rect.move(enemy_square_3, -5, 0)
    enemy_square_4 = pygame.Rect.move(enemy_square_4, -5, 0)
    enemy_square_5 = pygame.Rect.move(enemy_square_5, -5, 0) 
    enemy_square_6 = pygame.Rect.move(enemy_square_6, -5, 0)  
    enemy_square_7 = pygame.Rect.move(enemy_square_7, -5, 0)
    enemy_square_8 = pygame.Rect.move(enemy_square_8, -5, 0)
    enemy_square_9 = pygame.Rect.move(enemy_square_9, -5, 0)
    enemy_square_10 = pygame.Rect.move(enemy_square_10, -5, 0)
    enemy_square_11 = pygame.Rect.move(enemy_square_11, -5, 0)
    enemy_square_12 = pygame.Rect.move(enemy_square_12, -5, 0)
    enemy_square_13 = pygame.Rect.move(enemy_square_13, -5, 0)
    if pygame.Rect.colliderect(the_square, enemy_square_1) == True or pygame.Rect.colliderect(the_square, enemy_square_2) == True or pygame.Rect.colliderect(the_square, enemy_square_3) == True or pygame.Rect.colliderect(the_square, enemy_square_4) == True or pygame.Rect.colliderect(the_square, enemy_square_5) == True or pygame.Rect.colliderect(the_square, enemy_square_6) == True or pygame.Rect.colliderect(the_square, enemy_square_7) == True or pygame.Rect.colliderect(the_square, enemy_square_8) == True or pygame.Rect.colliderect(the_square, enemy_square_9) == True or pygame.Rect.colliderect(the_square, enemy_square_10) == True or pygame.Rect.colliderect(the_square, enemy_square_11) == True or pygame.Rect.colliderect(the_square, enemy_square_12) == True or pygame.Rect.colliderect(the_square, enemy_square_13) == True:
        print("Game Over!")
        pygame.quit()
        sys.exit()
    if the_square[1] <= 0 or the_square[1] >= 500:
        print("Game Over!")
        pygame.quit()
        sys.exit()
    if enemy_square_1[0] == -20:
        # Red squares reach the other end of the screen, so they all get reset
        random_list_of_y_coords = random.sample(range(0, 500, 10), 13)
        enemy_square_1 = pygame.Rect(480, random_list_of_y_coords[0], 10, 10)
        enemy_square_2 = pygame.Rect(480, random_list_of_y_coords[1], 10, 10)
        enemy_square_3 = pygame.Rect(480, random_list_of_y_coords[2], 10, 10)
        enemy_square_4 = pygame.Rect(480, random_list_of_y_coords[3], 10, 10)
        enemy_square_5 = pygame.Rect(480, random_list_of_y_coords[4], 10, 10)
        enemy_square_6 = pygame.Rect(480, random_list_of_y_coords[5], 10, 10)
        enemy_square_7 = pygame.Rect(480, random_list_of_y_coords[6], 10, 10)
        enemy_square_8 = pygame.Rect(480, random_list_of_y_coords[7], 10, 10)
        enemy_square_9 = pygame.Rect(480, random_list_of_y_coords[8], 10, 10)
        enemy_square_10 = pygame.Rect(480, random_list_of_y_coords[9], 10, 10)
        enemy_square_11 = pygame.Rect(480, random_list_of_y_coords[10], 10, 10)
        enemy_square_12 = pygame.Rect(480, random_list_of_y_coords[11], 10, 10)
        enemy_square_13 = pygame.Rect(480, random_list_of_y_coords[12], 10, 10)
        shooty_square_1 = pygame.Rect(490, random_list_of_y_coords[0], 10, 10)
        shooty_square_2 = pygame.Rect(490, random_list_of_y_coords[1], 10, 10)
        shooty_square_3 = pygame.Rect(490, random_list_of_y_coords[2], 10, 10)
        shooty_square_4 = pygame.Rect(490, random_list_of_y_coords[3], 10, 10)
        shooty_square_5 = pygame.Rect(490, random_list_of_y_coords[4], 10, 10)
        shooty_square_6 = pygame.Rect(490, random_list_of_y_coords[5], 10, 10)
        shooty_square_7 = pygame.Rect(490, random_list_of_y_coords[6], 10, 10)
        shooty_square_8 = pygame.Rect(490, random_list_of_y_coords[7], 10, 10)
        shooty_square_9 = pygame.Rect(490, random_list_of_y_coords[8], 10, 10)
        shooty_square_10 = pygame.Rect(490, random_list_of_y_coords[9], 10, 10)
        shooty_square_11 = pygame.Rect(490, random_list_of_y_coords[10], 10, 10)
        shooty_square_12 = pygame.Rect(490, random_list_of_y_coords[11], 10, 10)
        shooty_square_13 = pygame.Rect(490, random_list_of_y_coords[12], 10, 10)
        pygame.mixer.Sound.play(laser_sound)
        # Limits the tick rate at 250 (which is the game's state for neat)
        if increase_speed == 200:
            pass
        else:
            increase_speed += 5
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit() 
            if event.key == pygame.K_w:
                the_square = pygame.Rect.move(the_square, 0, -10)
            if event.key == pygame.K_s:
                the_square = pygame.Rect.move(the_square, 0, 10)       