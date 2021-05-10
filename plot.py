import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import json

import numpy as np
class Plot:
    def __init__(self):

        self.reward = np.array([])
        self.actions = np.array([])

    def read_jason(self):


        # with open('./data/data_01.json', 'r') as outfile:
        #     obj = json.load(outfile)


        # data = obj["data"]

        # # print(data)
        count = 0
        # for i in data:  
        #     print(i["action"])
        #     self.reward = np.append(self.reward, [i["reward"]])    
        #     self.actions = np.append(self.actions, [count])
        #     count+=1    
        #     # print(i["action"], i["reward"])

        with open('./data/data_08.json', 'r') as outfile:
            obj = json.load(outfile)


        data = obj["data1"]
        
        # print(data)
       
        for index in range(len(data)-1):  
            # print(data[index]['state'][1][0])
            # return  
            if data[index]['state'][1][0] < data[index+1]['state'][1][0]:
                
                
            # if data[index-1]["reward"] > data[index]["reward"]:
                # print(i["action"])
                self.reward = np.append(self.reward, [data[index-1]["total_reward"]])    
                self.actions = np.append(self.actions, [count]) 
                count+=1    
            # print(i["action"], i["reward"])
        print(self.reward)


        
        with open('./data/data_09.json', 'r') as outfile:
            obj = json.load(outfile)


        data = obj["data1"]

        # print(data)
       
        for index in range(len(data)-1):  
            if data[index]['state'][1][0] < data[index+1]['state'][1][0]:
            # if data[index-1]["reward"] > data[index]["reward"]:
                # print(i["action"])
                self.reward = np.append(self.reward, [data[index-1]["total_reward"]])    
                self.actions = np.append(self.actions, [count]) 
                count+=1    
            # print(i["action"], i["reward"])
        print(self.reward)

        
        with open('./data/data_10.json', 'r') as outfile:
            obj = json.load(outfile)


        data = obj["data1"]

        # # print(data)
        for index in range(len(data)-1):  
            if data[index]['state'][1][0] < data[index+1]['state'][1][0]:

            # if data[index-1]["reward"] > data[index]["reward"]:
                # print(i["action"])
                self.reward = np.append(self.reward, [data[index-1]["total_reward"]])    
                self.actions = np.append(self.actions, [count]) 
                count+=1     
            # print(i["action"], i["reward"])
        # print(self.reward)

    # Data for plotting
    def plot(self):

        import matplotlib
        import matplotlib.pyplot as plt

        print(len(self.actions))
        fig, ax = plt.subplots()
        ax.plot(self.actions, self.reward)

        ax.set(xlabel='No of epochs', ylabel='Total Rewad ',
            title=' Reward on each epoch')
        ax.grid()

        fig.savefig("test.png")
        plt.show()

plt = Plot()
plt.read_jason()

plt.plot()