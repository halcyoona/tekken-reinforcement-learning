import time
import random
# import tensorflow as tf   
# import numpy as np
from ddqn_agent import DDQNAgent
# from gameController.combos import pressKey
from gameController.keysClass import *
import json
from gettingHealthBar import States




class pressKey():
    

    def buttonPress(self,button):
        keys = Keys()
        keys.directKey(button)
        sleep(0.1)
        keys.directKey(button, keys.key_release)
        sleep(0.7)


class Enviroment:

    def __init__(self):

        self.button = pressKey()
        self.stateInstance = States()

        
        self.agent = DDQNAgent()

        # self.agent.load()
        



        self.actions = {
            "0": [1, 0, 0, 0, 0, 0, 0, 0 ],
            "1": [0, 1, 0, 0, 0, 0, 0, 0 ],
            "2": [0, 0, 1, 0, 0, 0, 0, 0 ],
            "3": [0, 0, 0, 1, 0, 0, 0, 0 ],
            "4": [0, 0, 0, 0, 1, 0, 0, 0 ],
            "5": [0, 0, 0, 0, 0, 1, 0, 0 ],
            "6": [0, 0, 0, 0, 0, 0, 1, 0 ],
            "7": [0, 0, 0, 0, 0, 0, 0, 1 ],
            "8": [0, 0, 0, 0, 0, 0, 0, 0 ],
        }
        self.actions_keyboard = {
            "0": "a",
            "1": "s",
            "2": "x",
            "3": "z",
            "4": "a",
            "5": "s",
            "6": "x",
            "7": "z"
        }


    def training(self, count):
              
        
        with open('./data/data_01.json', 'r') as outfile:
            obj = json.load(outfile)

        

        data = obj["data"+str(count)]

        for i in data:      
            self.agent.train(i["state"], i["action"], i["next_state"], i["reward"], i["done"])
        
        self.agent.save()

    ############################################################

    def enviromnet(self,state, done, time, state_img):
        
        actionDigit = int(self.agent.getAction(state_img))
        if actionDigit > 8 or actionDigit < 0:
            print("Not found")
            actionDigit = 0
        action = self.actions[str(actionDigit)]
        

    ############################################################

        action_keboard = self.actions_keyboard[str(actionDigit)]

        # preform action
        self.button.buttonPress(action_keboard)

        # state features evaluations
        health = self.stateInstance.stateHealthCalculate(state[0])
        game_time = [time,0]

        next_state = [ health, game_time] 

        # 
        reward = self.agent.getReward(state)
        automated_reward = self.agent.getAutomatedReward( state_img)
        

    ############################################################

        

        if done:
            done=False
        
        # print("state: ", state)
        # # print("total_reward: ", total_reward)
        # print("done: ", done)
        # print("action: ", action)
        # print("next_state: ", next_state)
        # print("reward: ", reward)
        return [state, actionDigit, next_state, reward, done]
