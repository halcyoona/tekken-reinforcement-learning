# import retro
import time
import random
import tensorflow.compat.v1 as tf   
import numpy as np
from dqn_agent_tf1 import DQNAgent
# from gameController.combos import pressKey
from gameController.keysClass import *

from gettingHealthBar import States




class pressKey():
    

    def buttonPress(self,button):
        keys = Keys()
        keys.directKey(button)
        sleep(0.1)
        keys.directKey(button, keys.key_release)
        sleep(0.7)


def enviromnet(state, total_reward, done, count, time, traning_data):
    button = pressKey()
    stateInstance = States()

    tf.disable_v2_behavior()

    agent = DQNAgent()

    actions = {
        "0": [1, 0, 0, 0],
        "1": [0, 1, 0, 0],
        "2": [0, 0, 1, 0],
        "3": [0, 0, 0, 1]
        # "4": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        # "5": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        # "6": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        # "7": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        # "8": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        # "9": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        # "10": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        # "11": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    }
    actions_keyboard = {
        "0": "a",
        "1": "s",
        "2": "x",
        "3": "z",
        # "4": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        # "5": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        # "6": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        # "7": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],aaz
        # "8": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        # "9": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        # "10": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        # "11": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    }

    if count == 0:
        tf.train.list_variables('./saved_models')    
        tf.train.load_checkpoint('./saved_models')

    state = state
    total_reward  = total_reward
    done = done
    # while not done:
    actionDigit = agent.get_action(state)
    if actionDigit > 11 or actionDigit < 0:
        print("Not found")
        actionDigit = 3
    action = actions[str(actionDigit)]
    # print("ActionDigit:", actionDigit)
    # print("Action:", action)
    # print("State:", state)

############################################################

    action_keboard = actions_keyboard[str(actionDigit)]

    # preform action
    button.buttonPress(action_keboard)

    # state features evaluations
    health =stateInstance.stateHealthCalculate(state[0])
    game_time = [time,0]

    next_state = [ health, game_time] 

    # 
    reward = agent.get_reward(state)
    

############################################################


    
    # next_state, reward, done, info = env.step(action)
    if done:
        for i in traning_data:
            agent.train(i[0], i[1], i[2], [3], i[4])
    # env.render()
    total_reward += reward
    state = next_state
    # print("next_state:", next_state)
    # print("Reward:", reward)
    # print("Done:", done)
    # time.sleep(10)

# if ep % 1 == 0:
    # print("Completed Training Cycle: " + str(epoch) + " out of " + str(self.num_of_epoch))
    # print("Current Loss: " + str(loss))
    if done:
        saver = tf.train.Saver()
        saver.save(agent.sess, 'saved_models/testing')
        print("Model saved")
        count = 0

    # print("Episode: {}, total_rewards: {1.2f}".format(ep, total_reward))
    # print("Episode: ", ep)
    # print("total_reward: ", total_reward)
    return [state, total_reward, done, action, next_state, reward]

if __name__ == "__main__":
    enviromnet()