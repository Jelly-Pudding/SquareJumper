import os
import neat
import pygame
import sys
import random
import pickle

local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config_file_for_neat.txt')

#print(config_path)

random_list_of_y_coords = random.sample(range(0, 500, 20), 5)

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.font.init()
myfont = pygame.font.SysFont("arial", 14)
the_square = pygame.Rect(10, 240, 10, 10)
enemy_square_1 = pygame.Rect(490, random_list_of_y_coords[0], 10, 10)
enemy_square_2 = pygame.Rect(490, random_list_of_y_coords[1], 10, 10)
enemy_square_3 = pygame.Rect(490, random_list_of_y_coords[2], 10, 10)
enemy_square_4 = pygame.Rect(490, random_list_of_y_coords[3], 10, 10)
enemy_square_5 = pygame.Rect(490, random_list_of_y_coords[4], 10, 10)
force_to_move_square1 = pygame.Rect(490, 240, 10, 10)
force_to_move_square2 = pygame.Rect(490, 230, 10, 10)
force_to_move_square3 = pygame.Rect(490, 250, 10, 10)

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
    pygame.draw.rect(screen, (255, 0, 0), force_to_move_square1)
    pygame.draw.rect(screen, (255, 0, 0), force_to_move_square2)
    pygame.draw.rect(screen, (255, 0, 0), force_to_move_square3)
    pygame.display.update()

running = True

count = 0

def get_input_for_neat(*args):
    input_list = []
    for square in args:
        input_list.append(square[1])
        input_list.append(square[1] + 10)
    return input_list
generation = 0
def eval_genomes(genomes, config):
    printed_fitness = 0
    global force_to_move_square1, force_to_move_square2, force_to_move_square3, generation, enemy_square_1, enemy_square_2, enemy_square_3, enemy_square_4, enemy_square_5, the_square
    generation += 1
    the_square = pygame.Rect(10, 240, 10, 10)
    random_list_of_y_coords = random.sample(range(0, 500, 10), 5)
    enemy_square_1 = pygame.Rect(490, random_list_of_y_coords[0], 10, 10)
    enemy_square_2 = pygame.Rect(490, random_list_of_y_coords[1], 10, 10)
    enemy_square_3 = pygame.Rect(490, random_list_of_y_coords[2], 10, 10)
    enemy_square_4 = pygame.Rect(490, random_list_of_y_coords[3], 10, 10)
    enemy_square_5 = pygame.Rect(490, random_list_of_y_coords[4], 10, 10)
    force_to_move_square1 = pygame.Rect(490, 240, 10, 10)
    force_to_move_square2 = pygame.Rect(490, 230, 10, 10)
    force_to_move_square3 = pygame.Rect(490, 250, 10, 10)
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
        clock.tick(200)        
        displayer(the_square_list)
        screen.fill((0,0,0))
        still_alive = myfont.render("Still alive: " + str(len(the_square_list)), False, (255, 255, 255))
        screen.blit(still_alive,(5,0))
        print_fitness = myfont.render("Fitness: " + str(printed_fitness), False, (255, 255, 255))
        screen.blit(print_fitness,(100,0))
        generation_num = myfont.render("Generation: " + str(generation), False, (255, 255, 255))
        screen.blit(generation_num,(200,0))
        enemy_square_1 = pygame.Rect.move(enemy_square_1, -5, 0)  
        enemy_square_2 = pygame.Rect.move(enemy_square_2, -5, 0)
        enemy_square_3 = pygame.Rect.move(enemy_square_3, -5, 0)
        enemy_square_4 = pygame.Rect.move(enemy_square_4, -5, 0)
        enemy_square_5 = pygame.Rect.move(enemy_square_5, -5, 0) 
        force_to_move_square1 = pygame.Rect.move(force_to_move_square1, -5, 0) 
        force_to_move_square2 = pygame.Rect.move(force_to_move_square2, -5, 0) 
        force_to_move_square3 = pygame.Rect.move(force_to_move_square3, -5, 0) 
        # If an enemy square hits our green square, the game ends
        for idx, square in enumerate(the_square_list):
            if pygame.Rect.colliderect(square, force_to_move_square1) == True or pygame.Rect.colliderect(square, force_to_move_square2) == True or pygame.Rect.colliderect(square, force_to_move_square3) == True or pygame.Rect.colliderect(square, enemy_square_1) == True or pygame.Rect.colliderect(square, enemy_square_2) == True or pygame.Rect.colliderect(square, enemy_square_3) == True or pygame.Rect.colliderect(square, enemy_square_4) == True or pygame.Rect.colliderect(square, enemy_square_5) == True:
                genome_list[idx].fitness -= 100.0
                the_square_list.pop(idx)
                genome_list.pop(idx)
                network_list.pop(idx)
                continue
            # Forces it to play within the screen
            if square[1] <= 0 or square[1] >= 500:
                genome_list[idx].fitness -= 100.0
                the_square_list.pop(idx)
                genome_list.pop(idx)
                network_list.pop(idx)
        if the_square_list == []:
            break
        if enemy_square_1[0] == -20:
            # Red squares reach the other end of the screen, so they all get reset
            random_list_of_y_coords = random.sample(range(0, 500, 10), 5)
            enemy_square_1 = pygame.Rect(490, random_list_of_y_coords[0], 10, 10)
            enemy_square_2 = pygame.Rect(490, random_list_of_y_coords[1], 10, 10)
            enemy_square_3 = pygame.Rect(490, random_list_of_y_coords[2], 10, 10)
            enemy_square_4 = pygame.Rect(490, random_list_of_y_coords[3], 10, 10)
            enemy_square_5 = pygame.Rect(490, random_list_of_y_coords[4], 10, 10)
            force_to_move_square1 = pygame.Rect(490, 240, 10, 10)
            force_to_move_square2 = pygame.Rect(490, 230, 10, 10)
            force_to_move_square3 = pygame.Rect(490, 250, 10, 10)
            printed_fitness += 1
            # It must have survived another round, so the network gets rewarded
            for idx, square in enumerate(the_square_list):
                genome_list[idx].fitness += 1.0
        neural_net_input = get_input_for_neat(square, enemy_square_1, enemy_square_2, enemy_square_3, enemy_square_4, enemy_square_5)
        for idx, square in enumerate(the_square_list):
            output = network_list[idx].activate(neural_net_input)
            max_value = max(output)
            max_index = output.index(max_value)
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
    winner = p.run(eval_genomes, 100)

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