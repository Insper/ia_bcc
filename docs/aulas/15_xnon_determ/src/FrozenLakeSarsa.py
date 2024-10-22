from IPython.display import clear_output
import gymnasium as gym
import numpy as np
from Sarsa import Sarsa
from numpy import loadtxt
import warnings
warnings.simplefilter("ignore")

def print_action(action):
    if action == 0:
        print("LEFT")
    elif action == 1: 
        print("DOWN")
    elif action == 2: 
        print("RIGHT")
    elif action == 3:
        print("UP")

# exemplo de ambiente nao determinístico
env = gym.make('FrozenLake-v1', render_mode='ansi').env

# only execute the following lines if you want to create a new q-table
#qlearn = Sarsa(env, alpha=0.2, gamma=0.95, epsilon=0.8, epsilon_min=0.0001, epsilon_dec=0.9999, episodes=50000)
#q_table = qlearn.train('data/q-table-frozen-lake-sarsa.csv','results/frozen_lake_sarsa')
q_table = loadtxt('data/q-table-frozen-lake-sarsa.csv', delimiter=',')

env = gym.make('FrozenLake-v1', render_mode='human').env
(state, _) = env.reset()
epochs = 0
rewards = 0
done = False
    
while not done:
    action = np.argmax(q_table[state])
    print_action(action)
    state, reward, done, _, info = env.step(action)
    rewards += reward
    epochs += 1

print("\n")
print("Timesteps taken: {}".format(epochs))
print("Rewards: {}".format(rewards))