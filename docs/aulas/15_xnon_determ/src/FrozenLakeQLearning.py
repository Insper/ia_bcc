from IPython.display import clear_output
import gymnasium as gym
import numpy as np
from QLearning import QLearning
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

qlearn = QLearning(env, alpha=0.1, gamma=0.99, epsilon=0.8, epsilon_min=0.01, epsilon_dec=1, episodes=20_000)
q_table = qlearn.train('data/q-table-frozen-lake-qlearning.csv','results/frozen_lake_qlearning','results/rewards_frozen_lake_qlearning.csv')
#q_table = loadtxt('data/q-table-frozen-lake-qlearning.csv', delimiter=',')

env = gym.make('FrozenLake-v1', render_mode='human').env

(state, _) = env.reset()
epochs = 0
rewards = 0
done = False
    
while not done:
    action = np.argmax(q_table[state])
    print_action(action)
    state, reward, done, _, info = env.step(action)
    epochs += 1
    rewards += reward

print("\n")
print("Timesteps taken: {}".format(epochs))
print("Rewards: {}".format(rewards))