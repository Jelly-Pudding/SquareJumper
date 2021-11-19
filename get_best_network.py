from train import *

def run_old_checkpoint(config_file):
      config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
      p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-1')
      p.add_reporter(neat.StdOutReporter(True))
      stats = neat.StatisticsReporter()
      p.add_reporter(stats)
      #p.add_reporter(neat.Checkpointer(1))
      winner = p.run(eval_genomes, 1)
      winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
      return winner_net

winner_net = run_old_checkpoint(config_path)

fh = open("network.pkl", 'wb')
pickle.dump(winner_net, fh)
fh.close()