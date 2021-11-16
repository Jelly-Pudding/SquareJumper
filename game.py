import os
import neat
import pygame
import sys
import random
import pickle

local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config_file_for_neat.txt')

#print(config_path)

random_list_of_y_coords = random.sample(range(0, 500, 20), 10)

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.font.init()
myfont = pygame.font.SysFont("arial", 14)
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

pygame.display.set_caption("Square Mover")
clock = pygame.time.Clock()

def displayer(squarelist):
    for i, square in enumerate(squarelist):
        pygame.draw.rect(screen, (0, 255, 0), square)
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
    pygame.draw.rect(screen, (0, 0, 255), shooty_square_1)
    pygame.draw.rect(screen, (0, 0, 255), shooty_square_2)
    pygame.draw.rect(screen, (0, 0, 255), shooty_square_3)
    pygame.draw.rect(screen, (0, 0, 255), shooty_square_4)
    pygame.draw.rect(screen, (0, 0, 255), shooty_square_5)
    pygame.draw.rect(screen, (0, 0, 255), shooty_square_6)
    pygame.draw.rect(screen, (0, 0, 255), shooty_square_7)
    pygame.draw.rect(screen, (0, 0, 255), shooty_square_8)
    pygame.draw.rect(screen, (0, 0, 255), shooty_square_9)
    pygame.draw.rect(screen, (0, 0, 255), shooty_square_10)
    
    pygame.display.update()

running = True
count = 0
generation = -1
countyep = 0
def eval_genomes(genomes, config):
    printed_fitness = 0
    global countyep, shooty_square_1, shooty_square_2, shooty_square_3, shooty_square_4, shooty_square_5, shooty_square_6, shooty_square_7, shooty_square_8, shooty_square_9, shooty_square_10, generation, enemy_square_1, enemy_square_2, enemy_square_3, enemy_square_4, enemy_square_5, enemy_square_6, enemy_square_7, enemy_square_8, enemy_square_9, enemy_square_10, the_square
    generation += 1
    the_square = pygame.Rect(10, 240, 10, 10)
    random_list_of_y_coords = random.sample(range(0, 500, 10), 10)
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
    the_square_list = []
    genome_list = []
    network_list = []
    for genome_id, genome in genomes:
        genome.fitness = 0.0
        the_square_list.append(the_square)
        genome_list.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        network_list.append(net)
    running = True
    while running == True:
        clock.tick(120)        
        screen.fill((0,0,0))
        still_alive = myfont.render("Still alive: " + str(len(the_square_list)), False, (255, 255, 255))
        screen.blit(still_alive,(5,0))
        print_fitness = myfont.render("Fitness: " + str(printed_fitness), False, (255, 255, 255))
        screen.blit(print_fitness,(100,0))
        generation_num = myfont.render("Generation: " + str(generation), False, (255, 255, 255))
        screen.blit(generation_num,(200,0))
        displayer(the_square_list)
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
        # If an enemy square hits our green square, the game ends
        for i in range(len(the_square_list) -1, -1, -1):
            square = the_square_list[i]
            if pygame.Rect.colliderect(square, enemy_square_1) == True or pygame.Rect.colliderect(square, enemy_square_2) == True or pygame.Rect.colliderect(square, enemy_square_3) == True or pygame.Rect.colliderect(square, enemy_square_4) == True or pygame.Rect.colliderect(square, enemy_square_5) == True or pygame.Rect.colliderect(square, enemy_square_6) == True or pygame.Rect.colliderect(square, enemy_square_7) == True or pygame.Rect.colliderect(square, enemy_square_8) == True or pygame.Rect.colliderect(square, enemy_square_9) == True or pygame.Rect.colliderect(square, enemy_square_10) == True:
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
        if the_square_list == []:
            break
        if enemy_square_1[0] == -20:
            # Red squares reach the other end of the screen, so they all get reset
            random_list_of_y_coords = random.sample(range(0, 500, 10), 10)
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
            printed_fitness += 1
            # It must have survived another round, so the network gets rewarded
            for idx, square in enumerate(the_square_list):
                genome_list[idx].fitness += 1.0
        for idx, square in enumerate(the_square_list):
            y = 0
            try:
                # If the colour at 490 at the opposite end of the screen from the green square is blue, there's an enemy 
                if pygame.Surface.get_at(screen, (490, the_square_list[idx][1])) == (0, 0, 255, 255):
                    countyep += 1
                    #print("Yep!" + str(countyep))
                    #print("\n")
                    y = 1
                # Checks nine pixels down because the green square's bottom can sometimes touch the top of an enemy square
                if pygame.Surface.get_at(screen, (490, the_square_list[idx][1]+9)) == (0, 0, 255, 255):
                    countyep += 1
                    #print("ADDED 9!" + str(countyep))
                    #print("\n")
                    y = 1
            # There's an Index Error if the green square goes to the bottom of the board. This is not an ideal place to be anyway,
            # so the input assumes there is an enemy at the other end 
            except IndexError:
                #print("Out of range (bottom of screen) = True!")    
                y = 1      
            output = network_list[idx].activate((the_square_list[idx][1], y))
            #print(output)
            max_value = max(output)
            max_index = output.index(max_value)
            #print(max_index)
            if max_index == 0:
                the_square_list[idx] = pygame.Rect.move(square, 0, -5)
            elif max_index == 1:
                pass
            elif max_index == 2:
                the_square_list[idx] = pygame.Rect.move(square, 0, 5)
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
    p.add_reporter(neat.Checkpointer(50))

    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 1)

    # Display the winning genome.
    # print('\nBest genome:\n{!s}'.format(winner))

    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-919')
    #winner = p.run(eval_genomes, 10)
    #print('\nBest genome:\n{!s}'.format(winner))
    #return winner
run(config_path)

'''
def run_old_checkpoint(config_file):
      config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
      p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-996')
      p.add_reporter(neat.StdOutReporter(True))
      stats = neat.StatisticsReporter()
      p.add_reporter(stats)
      p.add_reporter(neat.Checkpointer(5))
      winner = p.run(eval_genomes, 250)
      winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
      return winner_net

winner_net = run_old_checkpoint(config_path)

fh = open("network.pkl", 'wb')
pickle.dump(winner_net, fh)
fh.close()

fh = open("network.pkl", 'rb')
bestnetwork = pickle.load(fh)
fh.close()

'''