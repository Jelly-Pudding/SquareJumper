import os
import neat
import pygame
import sys
import random
import pickle

local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config_file_for_neat.txt')

#print(config_path)

random_list_of_y_coords = random.sample(range(0, 500, 20), 13)

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.font.init()
myfont = pygame.font.SysFont("arial", 14)
smallfont = pygame.font.SysFont("arial", 11)
the_square = pygame.Rect(10, 240, 10, 10)
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

pygame.display.set_caption("Square Mover")
clock = pygame.time.Clock()

def displayer(squarelist):
    for i, square in enumerate(squarelist):
        pygame.draw.rect(screen, (0, 255, 0), square["square"])
    #pygame.draw.rect(screen, (0, 255, 0), the_square)
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
count = 0
generation = -1
#countyep = 0
def eval_genomes(genomes, config):
    printed_fitness = 0
    global y, max_index, shooty_square_1, shooty_square_2, shooty_square_3, shooty_square_4, shooty_square_5, shooty_square_6, shooty_square_7, shooty_square_8, shooty_square_9, shooty_square_10, shooty_square_11, shooty_square_12, shooty_square_13, generation, enemy_square_1, enemy_square_2, enemy_square_3, enemy_square_4, enemy_square_5, enemy_square_6, enemy_square_7, enemy_square_8, enemy_square_9, enemy_square_10, enemy_square_11, enemy_square_12, enemy_square_13, the_square
    generation += 1
    the_square = pygame.Rect(10, 240, 10, 10)
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
    # To show all the different networks of a generation tackle the game at the same time,
    # everything must be sorted into lists which can then be accessed through iteration
    the_square_list = []
    genome_list = []
    network_list = []
    for genome_id, genome in genomes:
        genome.fitness = 0.0
        the_square_list.append({"square": the_square, "direction_change": False, "threshold": 50})
        genome_list.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        network_list.append(net)
    running = True
    while running == True:
        # Time goes faster at higher tick rates. 250 is quite fast, but the network will be able to handle it. 
        clock.tick(250)        
        screen.fill((0,0,0))
        # Represents the input node as a green circle
        for k in config.genome_config.input_keys:
            pygame.draw.circle(screen, (0, 255, 0), (25, 25), 5, 0)
        # Represents the output nodes as green circles if activated, and red circles if not activated
        # Lines are also drawn between the input node and all output nodes to represent the connections
        change_line = 0
        for idx, cg in enumerate(genome.connections.values()):
            try:
                if max_index == idx:
                    pygame.draw.line(screen,(0, 255, 0),(25,25),(50,10 + change_line),1)
                    pygame.draw.circle(screen, (0, 255, 0), (50, 10 + change_line), 5, 0)
                else:
                    pygame.draw.line(screen,(255, 0, 0),(25,25),(50,10 + change_line),1)
                    pygame.draw.circle(screen, (255, 0, 0), (50, 10 + change_line), 5, 0)
            # There is a NameError if max_index has not been defined yet
            except NameError:
                continue
            change_line += 15
        # Shows the input the network receives
        try:
            y_input = smallfont.render(str(y), False, (255, 255, 255))
            screen.blit(y_input,(7, 19))
        # There is a NameError if y has not been defined yet
        except NameError:
            pass
        # Shows what each output node does when activated
        up = smallfont.render("up", False, (255, 255, 255))
        screen.blit(up, (60, 2))
        straight = smallfont.render("stay", False, (255, 255, 255))
        screen.blit(straight, (60, 19))
        down = smallfont.render("down", False, (255, 255, 255))
        screen.blit(down, (60, 35))
        # Displays general information for each generation
        still_alive = myfont.render("Still alive: " + str(len(the_square_list)), False, (255, 255, 255))
        screen.blit(still_alive,(200,0))
        print_fitness = myfont.render("Fitness: " + str(printed_fitness), False, (255, 255, 255))
        screen.blit(print_fitness,(285,0))
        generation_num = myfont.render("Generation: " + str(generation), False, (255, 255, 255))
        screen.blit(generation_num,(100,0))
        displayer(the_square_list)
        # Moves enemies to the left by five pixels
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
        # If an enemy square hits our green square, the game ends
        for i in range(len(the_square_list) -1, -1, -1):
            square = the_square_list[i]["square"]
            if pygame.Rect.colliderect(square, enemy_square_1) == True or pygame.Rect.colliderect(square, enemy_square_2) == True or pygame.Rect.colliderect(square, enemy_square_3) == True or pygame.Rect.colliderect(square, enemy_square_4) == True or pygame.Rect.colliderect(square, enemy_square_5) == True or pygame.Rect.colliderect(square, enemy_square_6) == True or pygame.Rect.colliderect(square, enemy_square_7) == True or pygame.Rect.colliderect(square, enemy_square_8) == True or pygame.Rect.colliderect(square, enemy_square_9) == True or pygame.Rect.colliderect(square, enemy_square_10) == True or pygame.Rect.colliderect(square, enemy_square_11) == True or pygame.Rect.colliderect(square, enemy_square_12) == True or pygame.Rect.colliderect(square, enemy_square_13) == True:
                genome_list[i].fitness -= 100.0
                the_square_list.pop(i)
                genome_list.pop(i)
                network_list.pop(i)
                continue
            # Forces it to play within the screen
            if square[1] <= 0 or square[1] >= 500:
                genome_list[i].fitness -= 100.0
                the_square_list.pop(i)
                genome_list.pop(i)
                network_list.pop(i)
            try:
                if genome_list[i].fitness == 300:
                    the_square_list.pop(i)
                    genome_list.pop(i)
                    network_list.pop(i)
            # There is sometimes an IndexError if the genome has already been popped
            except IndexError:
                pass
        if the_square_list == []:
            break
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
            printed_fitness += 1
            # It must have survived another round, so the network gets rewarded
            for idx, square in enumerate(the_square_list):
                genome_list[idx].fitness += 1.0
        # Gets input for the network
        for idx, square in enumerate(the_square_list):
            # The default value for the input is 0
            y = 0
            # If the square reaches a certain section of the screen, we need to record this
            # to encourage it to not continue in that direction (it will eventually die if it
            # continues in one direction as it will touch the top or bottom of the screen)
            if the_square_list[idx]["square"][1] == 200 and the_square_list[idx]["threshold"] != 200:
                the_square_list[idx]["direction_change"] = not the_square_list[idx]["direction_change"]
                the_square_list[idx]["threshold"] = 200
            elif the_square_list[idx]["square"][1] == 300 and the_square_list[idx]["threshold"] != 300:
                the_square_list[idx]["direction_change"] = not the_square_list[idx]["direction_change"]
                the_square_list[idx]["threshold"] = 300
            try:
                # If the colour at the opposite end of the screen from the green square is orange (which represents
                # an unmoving 'shooter'), then there's a red-squared enemy on the way 
                if pygame.Surface.get_at(screen, (490, the_square_list[idx]["square"][1])) == (255,165,0, 255):
                    if the_square_list[idx]["direction_change"] == True:
                        y = 1
                    elif the_square_list[idx]["direction_change"] == False:
                        y = -1
                # Checks nine pixels down because the green square's bottom can sometimes touch the top of an enemy square
                elif pygame.Surface.get_at(screen, (490, the_square_list[idx]["square"][1]+9)) == (255,165,0, 255):
                    if the_square_list[idx]["direction_change"] == True:
                        y = 1
                    elif the_square_list[idx]["direction_change"] == False:
                        y = -1
            # There's an Index Error if the green square goes to the bottom of the screen (as nine pixels cannot be added in this case).
            except IndexError:
                #print("Out of range (bottom of screen) = True!")    
                pass
            output = network_list[idx].activate(([y]))
            #print(output)
            max_value = max(output)
            # Gets the index of the element with the highest value in the output list
            max_index = output.index(max_value)
            #print(max_index)
            # Depending upon the index, the green square will move down, remain stationary, or move upward
            if max_index == 0:
                the_square_list[idx]["square"] = pygame.Rect.move(square["square"], 0, -1)
            elif max_index == 1:
                pass
            elif max_index == 2:
                the_square_list[idx]["square"] = pygame.Rect.move(square["square"], 0, 1)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # Uncomment if you want to add neat checkpoint files
    #p.add_reporter(neat.Checkpointer(1))

    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 5)

    # Display the winning genome.
    # print('\nBest genome:\n{!s}'.format(winner))

    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-919')
    #winner = p.run(eval_genomes, 10)
    #print('\nBest genome:\n{!s}'.format(winner))
    #return winner

# Only executes the run function if this file is accessed directly (as opposed to being imported)
if __name__ == "__main__":
    run(config_path)