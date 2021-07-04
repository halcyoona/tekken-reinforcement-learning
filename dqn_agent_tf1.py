
import random
import tensorflow.compat.v1 as tf   
import numpy as np
from agent import Agent
from q_network_tf1 import QNetwork


class DQNAgent(Agent):
    def __init__(self, env=0, discount_rate=0.97, learning_rate=0.01, epsilon=1.0):
        self.state_dim = (2,2)
        self.action_size = 8
        self.q_network = QNetwork(self.state_dim, self.action_size, learning_rate)

        self.gamma = discount_rate
        self.eps = epsilon
        self.learning_rate = learning_rate

        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())


    def getAction(self, state):
        q_state = self.q_network.getQState(self.sess, [state])
        action_greedy = np.argmax(q_state)
        action_random = np.random.randint(self.action_size)
        # action = action_random if random.random() < self.eps else action_greedy
        return action_random

    def getReward(self, state):
        reward = -5
        if state[0][0] > state[0][1]:
            reward = (state[0][0]/ state[0][1]) * state[1][0]

        if state[0][1] > state[0][0]:
            reward = -((state[0][0] / state[0][1]) * state[1][0])

        return reward

    def train(self, state, action, next_state, reward, done):
        q_next_state = self.q_network.getQState(self.sess, [next_state])
        q_state = self.q_network.getQState(self.sess, [state])
        q_next_state = (1-done) * q_next_state
        q_target = reward + (self.gamma * np.max(q_next_state) - np.max(q_state))
        self.q_network.updateModel(self.sess, [state], [action], [q_target])
        if done: self.eps = max(0.1, 0.99 * self.eps)


