from train import *

fh = open("network.pkl", 'rb')
bestnetwork = pickle.load(fh)
fh.close()

best_square = pygame.Rect(10, 240, 10, 10)

the_square = {"square": best_square, "direction_change": False, "threshold": 50}

score = 0

def display():
    pygame.draw.rect(screen, (0, 255, 0), the_square["square"])
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
while running:
    clock.tick(250)        
    screen.fill((0,0,0))
    score_text = myfont.render("Score: " + str(score), False, (255, 255, 255))
    screen.blit(score_text,(200,0))
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
    if pygame.Rect.colliderect(the_square["square"], enemy_square_1) == True or pygame.Rect.colliderect(the_square["square"], enemy_square_2) == True or pygame.Rect.colliderect(the_square["square"], enemy_square_3) == True or pygame.Rect.colliderect(the_square["square"], enemy_square_4) == True or pygame.Rect.colliderect(the_square["square"], enemy_square_5) == True or pygame.Rect.colliderect(the_square["square"], enemy_square_6) == True or pygame.Rect.colliderect(the_square["square"], enemy_square_7) == True or pygame.Rect.colliderect(the_square["square"], enemy_square_8) == True or pygame.Rect.colliderect(the_square["square"], enemy_square_9) == True or pygame.Rect.colliderect(the_square["square"], enemy_square_10) == True or pygame.Rect.colliderect(the_square["square"], enemy_square_11) == True or pygame.Rect.colliderect(the_square["square"], enemy_square_12) == True or pygame.Rect.colliderect(the_square["square"], enemy_square_13) == True:
        pygame.quit()
        sys.exit()
    if the_square["square"][1] <= 0 or the_square["square"][1] >= 500:
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
        score += 1
    y = 0
    if the_square["square"][1] == 200 and the_square["threshold"] != 200:
        the_square["direction_change"] = not the_square["direction_change"]
        the_square["threshold"] = 200
    elif the_square["square"][1] == 300 and the_square["threshold"] != 300:
        the_square["direction_change"] = not the_square["direction_change"]
        the_square["threshold"] = 300
    try:
        # If the colour at 490 at the opposite end of the screen from the green square is blue, there's an enemy 
        if pygame.Surface.get_at(screen, (490, the_square["square"][1])) == (255,165,0, 255):
            if the_square["direction_change"] == True:
                y = 1
            elif the_square["direction_change"] == False:
                y = -1
        # Checks nine pixels down because the green square's bottom can sometimes touch the top of an enemy square
        elif pygame.Surface.get_at(screen, (490, the_square["square"][1]+9)) == (255,165,0, 255):
            if the_square["direction_change"] == True:
                y = 1
            elif the_square["direction_change"] == False:
                y = -1
    # There's an Index Error if the green square goes to the bottom of the board.
    except IndexError:
        #print("Out of range (bottom of screen) = True!")    
        pass
    fh = open("network.pkl", 'rb')
    bestnetwork = pickle.load(fh)
    fh.close()
    output = bestnetwork.activate(([y]))
    max_value = max(output)
    max_index = output.index(max_value)
    if max_index == 0:
        the_square["square"] = pygame.Rect.move(the_square["square"], 0, -1)
    elif max_index == 1:
        pass
    elif max_index == 2:
        the_square["square"] = pygame.Rect.move(the_square["square"], 0, 1)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

