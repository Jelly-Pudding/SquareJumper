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
        printnow = False
        # Time goes faster at higher tick rates. 250 is quite fast, but the network will be able to handle it. 
        clock.tick(250)        
        screen.fill((0,0,0))

        # Represents the input node as a green circle
        
        for i in config.genome_config.input_keys:
            pygame.draw.circle(screen, (0, 255, 0), (25, 25), 5, 0)

        list_of_all_connections = []
        # Default value for layers. 
        # input layer and output layer will always be None
        layer_input = None
        layer_output = None
        for cg in genome.connections.values():
            # Default - it will be the second layer if the first node isn't the input node and the second node is one of the output nodes
            if cg.key[0] != -1:
                if cg.key[1] == 0 or cg.key[1] == 1 or cg.key[1] == 2:
                    layer_input = 2
                    # If the node has already been connected to from somewhere else, then the layer output value for that connection will be used
                    for idx in range(len(list_of_all_connections)):
                        if list_of_all_connections[idx]["second_node"] == cg.key[0]:
                            layer_input = list_of_all_connections[idx]["layer_output"]
                    layer_output = None
            # Default - it will be the second layer if the first node is the input node but the second node is not an output node
            if cg.key[0] == -1:
                if cg.key[1] != 0 and cg.key[1] != 1 and cg.key[1] != 2:
                    layer_input = None
                    layer_output = 2
            # This layer will be layer three or higher because the first node isn't the input node and the second node isn't an output node
            if cg.key[0] != -1 and cg.key[1] != 0 and cg.key[1] != 1 and cg.key[1] != 2:
                # Check if the input node for this connection was the output node for another connection
                for idx in range(len(list_of_all_connections)):
                    if list_of_all_connections[idx]["second_node"] == cg.key[0]:
                        # Equals none if an output node appears as the first node in the connection (which can happen)
                        if list_of_all_connections[idx]["layer_output"] == None:
                            # Because it has been reversed, a default value of 1 will be given. This value will get updated later.  
                            layer_input = 1
                            # Output equals None as it must be an output node
                            layer_output = None
                            print("it's none!")
                            print("\n")
                            print("\n")
                            print("\n")
                            print("\n")
                            print("\n")
                            print("\n")
                            print("\n")
                            print("\n")
                            print("\n")
                        elif list_of_all_connections[idx]["layer_output"] != None:
                            layer_input = list_of_all_connections[idx]["layer_output"]
                            # Take the layer of what is connecting to this node and add one (because it must be one layer further in the network)
                            layer_output = list_of_all_connections[idx]["layer_output"] + 1
            #fixes the reversed order if it does occur (where an output node appears as the first node)
            if cg.key[0] == 0 or cg.key[0] == 1 or cg.key[0] == 2:
                list_of_all_connections.append({"first_node": cg.key[1], "second_node": cg.key[0], "weight": cg.weight, "enabled": cg.enabled, "layer_input": layer_input, "layer_output": layer_output})
                printnow = True             
            else:
                list_of_all_connections.append({"first_node": cg.key[0], "second_node": cg.key[1], "weight": cg.weight, "enabled": cg.enabled, "layer_input": layer_input, "layer_output": layer_output})

        if printnow == True:
            print(list_of_all_connections) 

        # Updates the layer value of nodes to ensure the layer found is always the highest value the node has achieved 
        for i in range(len(list_of_all_connections)):
            # Deals with the input layer
            summed = []
            element = list_of_all_connections[i]["first_node"]
            if element != -1 and element != 0 and element != 1 and element != 2:
                for e in range(len(list_of_all_connections)):
                    if list_of_all_connections[e]["first_node"] == element:
                        summed.append(list_of_all_connections[e]["layer_input"])
                    if list_of_all_connections[e]["second_node"] == element:
                        summed.append(list_of_all_connections[e]["layer_output"])
                try:
                    maxxed = max(summed)
                    list_of_all_connections[i]["layer_input"] = maxxed
                except Exception as e:
                    print(e)
                    print(list_of_all_connections)
                    print(element)
                maxxed = max(summed)
                list_of_all_connections[i]["layer_input"] = maxxed
            elif element == -1 or element == 0 or element == 1 or element == 2:
                list_of_all_connections[i]["layer_input"] = None
            # Deals with the output layer
            summed = []
            element = list_of_all_connections[i]["second_node"]
            if element != -1 and element != 0 and element != 1 and element != 2: 
                for e in range(len(list_of_all_connections)):
                    if list_of_all_connections[e]["first_node"] == element:
                        summed.append(list_of_all_connections[e]["layer_input"])
                    if list_of_all_connections[e]["second_node"] == element:
                        summed.append(list_of_all_connections[e]["layer_output"])
                try:
                    maxxed = max(summed)
                    list_of_all_connections[i]["layer_output"] = maxxed
                except Exception as e:
                    print(e)
                    print(list_of_all_connections)
                    print(element)
                maxxed = max(summed)
                list_of_all_connections[i]["layer_output"] = maxxed
            elif element == -1 or element == 0 or element == 1 or element == 2:
                list_of_all_connections[i]["layer_output"] = None
               
                
        print(list_of_all_connections)




        hidden_connections = []
        change_line_output = 0
        push_back_for_hidden_layer = 0

        for dic in list_of_all_connections:
            # This means there will be nodes in the hidden layer (as either the first node isn't the input node, or the second node isn't one of the output nodes)
            if dic["first_node"] != -1 or dic["second_node"] != 0 and dic["second_node"] != 1 and dic["second_node"] != 2:
                push_back_for_hidden_layer = 50
                hidden_connections.append(dic)

        #print(list_of_all_connections)

        visible_connections = []

        output_0_index = next((index for (index, d) in enumerate(list_of_all_connections) if d["first_node"] == -1 and d["second_node"] == 0), None)
        if output_0_index != None:
            visible_connections.append(list_of_all_connections[output_0_index])
        output_1_index = next((index for (index, d) in enumerate(list_of_all_connections) if d["first_node"] == -1 and d["second_node"] == 1), None)
        if output_1_index != None:
            visible_connections.append(list_of_all_connections[output_1_index])
        output_2_index = next((index for (index, d) in enumerate(list_of_all_connections) if d["first_node"] == -1 and d["second_node"] == 2), None)
        if output_2_index != None:
            visible_connections.append(list_of_all_connections[output_2_index])

        output_0_position = 0
        output_1_position = 1
        output_2_position = 2

        # deals with the output layers
        if visible_connections != []:
            for dic in visible_connections:
                if dic["enabled"] == True:
                    if dic["weight"] > 0.7:
                        pygame.draw.line(screen,(0, 255, 0),(25,25),(50 + push_back_for_hidden_layer, 10 + change_line_output),3)
                    elif dic["weight"] > 0.5:
                        pygame.draw.line(screen,(0, 255, 0),(25,25),(50 + push_back_for_hidden_layer, 10 + change_line_output),2)
                    elif dic["weight"] > 0:
                        pygame.draw.line(screen,(0, 255, 0),(25,25),(50 + push_back_for_hidden_layer, 10 + change_line_output),1)
                    elif dic["weight"] < 0:
                        pygame.draw.line(screen,(255, 0, 0),(25,25),(50 + push_back_for_hidden_layer, 10 + change_line_output),1)
                pygame.draw.circle(screen, (0, 255, 0), (50 + push_back_for_hidden_layer, 10 + change_line_output), 5, 0)
                if dic["second_node"] == 0:
                    output_0_position = (50 + push_back_for_hidden_layer, 10 + change_line_output)
                elif dic["second_node"] == 1:
                    output_1_position = (50 + push_back_for_hidden_layer, 10 + change_line_output) 
                elif dic["second_node"] == 2:
                    output_2_position = (50 + push_back_for_hidden_layer, 10 + change_line_output)   
                change_line_output += 15


        # deals with connections from the first node to the hidden layer

        change_line_output = 0
        circle_positions = []
        if hidden_connections != []:
            for dic in hidden_connections:
                change_line_output += 6
                if dic["first_node"] == -1:
                    if dic["enabled"] == True:
                        pygame.draw.line(screen,(0, 255, 0), (25, 25), (80, 10 + change_line_output), 1)
                    pygame.draw.circle(screen, (0, 255, 0), (80, 10 + change_line_output), 5, 0)
                    circle_positions.append({"node": dic["second_node"], "position": (80, 10 + change_line_output)})

        # deals with connections between the hidden layer and the output

        if hidden_connections != []:
            for dic in hidden_connections:
                if dic["first_node"] != - 1:
                    if dic["second_node"] == 0:
                        circle_index = next((index for (index, d) in enumerate(circle_positions) if d["node"] == dic["first_node"]), None)
                        # Equals none when there's a second hidden layer... for example, node was 4 from circle, and from dic first node 
                        # it was 8 (8 was in second layer and connected to 0)
                        if circle_index == None:
                            #print(circle_positions)
                            #print(dic["first_node"])
                            #print(hidden_connections)
                            pass
                        the_circle_position = circle_positions[circle_index]["position"]
                        pygame.draw.line(screen, (0, 255, 0), the_circle_position, output_0_position, 1)
                    elif dic["second_node"] == 1:
                        circle_index = next((index for (index, d) in enumerate(circle_positions) if d["node"] == dic["first_node"]), None)
                        if circle_index == None:
                            #print(circle_positions)
                            #print(dic["first_node"])
                            #print(hidden_connections)
                            pass
                        the_circle_position = circle_positions[circle_index]["position"]
                        pygame.draw.line(screen, (0, 255, 0), the_circle_position, output_1_position, 1)
                    if dic["second_node"] == 2:
                        circle_index = next((index for (index, d) in enumerate(circle_positions) if d["node"] == dic["first_node"]), None)
                        if circle_index == None:
                            #print(circle_positions)
                            #print(dic["first_node"])
                            #print(hidden_connections)
                            pass
                        the_circle_position = circle_positions[circle_index]["position"]
                        pygame.draw.line(screen, (0, 255, 0), the_circle_position, output_2_position, 1)

        # Shows the input the network receives
        try:
            y_input = smallfont.render(str(y), False, (255, 255, 255))
            screen.blit(y_input,(7, 19))
        # There is a NameError if y has not been defined yet
        except NameError:
            pass
        
        # Displays general information for each generation
        still_alive = myfont.render("Still alive: " + str(len(the_square_list)), False, (255, 255, 255))
        screen.blit(still_alive,(200+push_back_for_hidden_layer,0))
        print_fitness = myfont.render("Fitness: " + str(printed_fitness), False, (255, 255, 255))
        screen.blit(print_fitness,(285+push_back_for_hidden_layer,0))
        generation_num = myfont.render("Generation: " + str(generation), False, (255, 255, 255))
        screen.blit(generation_num,(100+push_back_for_hidden_layer,0))
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
    winner = p.run(eval_genomes, 20)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-919')
    #winner = p.run(eval_genomes, 10)
    #print('\nBest genome:\n{!s}'.format(winner))
    #return winner

# Only executes the run function if this file is accessed directly (as opposed to being imported)
if __name__ == "__main__":
    run(config_path)