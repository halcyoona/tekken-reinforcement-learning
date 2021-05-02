
from dqn_agent_tf1 import DQNAgent
import tensorflow.compat.v1 as tf  
import json
def training():
    tf.disable_v2_behavior()
    agent = DQNAgent()
    
    tf.train.list_variables('./saved_models')    
    tf.train.load_checkpoint('./saved_models')

    with open('./data/data_04.json', 'r') as outfile:
        obj = json.load(outfile)

    

    data = obj["data1"]

    for i in data:      
        agent.train(i["state"], i["action"], i["next_state"], i["reward"], i["done"])
    
    saver = tf.train.Saver()
    saver.save(agent.sess, 'saved_models/testing')
    # print(i)

training()