
import random
import tensorflow as tf   
import numpy as np
from agent import Agent

from ddqn_network import DDQNetwork

from reward_network import CNN

class DDQNAgent(Agent):
    def __init__(self, learning_rate=0.01, discount_rate=0.97, epsilon=1.0):
        self.state_dim = ( 720, 1280, 3)
        self.action_size = 8
        self.network = DDQNetwork(self.state_dim, self.action_size, learning_rate, discount_rate, epsilon)
        self.reward_cnn = CNN(self.state_dim, self.action_size, learning_rate, discount_rate, epsilon)

        self.gamma = discount_rate
        self.eps = epsilon
        self.learning_rate = learning_rate


    
    def getAction(self, state):
        q_values = self.network.getQState(state)
        action_greedy = np.amax(q_values[0])
        action_random = np.random.randint(self.action_size)
        action = action_random if random.random() <= self.eps else action_greedy
        return action

    def getReward(self, state):
        reward = -5
        if state[0][0] > state[0][1]:
            reward = (state[0][0]/ state[0][1]) * state[1][0]

        if state[0][1] > state[0][0]:
            reward = -((state[0][0] / state[0][1]) * state[1][0])

        return reward

    def getAutomatedReward(self, state):
        return self.reward_cnn.getReward(state)

    def train(self, state, action, next_state, reward, done):
        q_next_values = self.network.getQState(next_state)
        q_values = self.network.getQState(state)
        q_next_values = (1-done) * np.amax(q_next_values[0])
        q_updated_value = reward + (self.gamma * np.amax(q_next_values))
        q_values[0][action] = q_updated_value
        self.network.updateModel(state, q_values)
        self.reward_cnn.updateModel(state, reward)
        if done: self.eps = max(0.1, 0.99 * self.eps)

    
    def load(self):
        self.network.loadModel()
    
    def save(self):
        self.network.saveModel()