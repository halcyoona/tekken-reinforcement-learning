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
        #     self.reward = np.append(self.reward, [i["total_reward"]])    
        #     self.actions = np.append(self.actions, [count])
        #     count+=1    
        #     # print(i["action"], i["total_reward"])

        with open('./data/data_02.json', 'r') as outfile:
            obj = json.load(outfile)


        data = obj["data"]

        # print(data)
       
        for i in data:  
            print(i["action"])
            self.reward = np.append(self.reward, [i["total_reward"]])    
            self.actions = np.append(self.actions, [count])
            count+=1    
            # print(i["action"], i["total_reward"])
        print(self.reward)


        
        with open('./data/data_04.json', 'r') as outfile:
            obj = json.load(outfile)


        data = obj["data1"]

        # print(data)
       
        for i in data:  
            print(i["action"])
            self.reward = np.append(self.reward, [i["total_reward"]])    
            self.actions = np.append(self.actions, [count]) 
            count+=1    
            # print(i["action"], i["total_reward"])
        print(self.reward)

        
        with open('./data/data_07.json', 'r') as outfile:
            obj = json.load(outfile)


        data = obj["data1"]

        # print(data)
       
        for i in data:  
            print(i["action"])
            self.reward = np.append(self.reward, [i["total_reward"]])    
            self.actions = np.append(self.actions, [count])
            count+=1    
            # print(i["action"], i["total_reward"])
        print(self.reward)

    # Data for plotting
    def plot(self):

        import matplotlib
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.plot(self.actions, self.reward)

        ax.set(xlabel='No of : actions', ylabel='Rewards ',
            title='Reward on actions (after next round reward will start from zero )')
        ax.grid()

        fig.savefig("test.png")
        plt.show()

plt = Plot()
plt.read_jason()

plt.plot()