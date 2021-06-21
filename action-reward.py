from os import terminal_size
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import json

from random import *

import numpy as np
class Plot:
    def __init__(self):

        self.reward = np.array([])
        self.actions = np.array([])

        self.flag_00 = True
        self.flag_01 = True
        self.flag_02 = True
        self.flag_03 = True

        self.reward_list = [0,0,0,0,-800,-200,-500,-300]
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

        


        
        with open('./data/data_01.json', 'r') as outfile:
            obj = json.load(outfile)


        data = obj["data"]

        # print(data)
       
        for index in range(len(data)-1): 

            if data[index]['action'] == [1,0,0,0] and self.flag_00 == True:
                self.reward_list[0] += data[index]['reward'] 
                self.flag_00 = False
                continue

            if data[index]['action'] == [0,1,0,0] and self.flag_01 == True:
                self.reward_list[1] += data[index]['reward'] 
                self.flag_01 = False
                continue
            if data[index]['action'] == [0,0,1,0] and self.flag_02 == True:
                self.reward_list[2] += data[index]['reward'] 
                self.flag_02 = False
                continue
            if data[index]['action'] == [0,0,0,1] and self.flag_03 == True:
                self.reward_list[3] += data[index]['reward'] 
                self.flag_03 = False
                continue

            if data[index]['action'] == [1,0,0,0] and self.flag_00 == False:
                self.reward_list[4] += data[index]['reward'] 
                self.flag_00 = True

            if data[index]['action'] == [0,1,0,0] and self.flag_01 == False:
                self.reward_list[5] += data[index]['reward'] 
                self.flag_01 = True

            if data[index]['action'] == [0,0,1,0] and self.flag_02 == False:
                self.reward_list[6] += data[index]['reward'] 
                self.flag_02 = True
            
            if data[index]['action'] == [0,0,0,1] and self.flag_03 == False:
                self.reward_list[7] += data[index]['reward'] 
                self.flag_03 = True

        
        with open('./data/data_10.json', 'r') as outfile:
            obj = json.load(outfile)


        data = obj["data1"]

        # # print(data)
        for index in range(len(data)-1):  
            if data[index]['action'] == [1,0,0,0] and self.flag_00 == True:
                self.reward_list[0] += data[index]['reward'] 
                self.flag_00 = False
                continue

            if data[index]['action'] == [0,1,0,0] and self.flag_01 == True:
                self.reward_list[1] += data[index]['reward'] 
                self.flag_01= False
                continue

            if data[index]['action'] == [0,0,1,0] and self.flag_02 == True:
                self.reward_list[2] += data[index]['reward'] 
                self.flag_02 == False
                continue
            
            if data[index]['action'] == [0,0,0,1] and self.flag_03 == True:
                self.reward_list[3] += data[index]['reward'] 
                self.flag_03 = False
                continue


            if data[index]['action'] == [1,0,0,0] and self.flag_00 == False:
                self.reward_list[4] += data[index]['reward'] 
                self.flag_00 = True

            if data[index]['action'] == [0,1,0,0] and self.flag_01 == False:
                self.reward_list[5] += data[index]['reward'] 
                self.flag_01 = True

            if data[index]['action'] == [0,0,1,0] and self.flag_02 == False:
                self.reward_list[6] += data[index]['reward'] 
                self.flag_02 = True
            
            if data[index]['action'] == [0,0,0,1] and self.flag_03 == False:
                self.reward_list[7] += data[index]['reward'] 
                self.flag_03 = True
            # print(i["action"], i["reward"])
        # print(self.reward)


        with open('./data/data_08.json', 'r') as outfile:
            obj = json.load(outfile)


        data = obj["data1"]
        
        # print(data)
       
        for index in range(len(data)-1):  
            # print(data[index]['state'][1][0])
            # return  
            if data[index]['action'] == [1,0,0,0] and self.flag_00 == True:
                self.reward_list[0] += data[index]['reward'] 
                self.flag_00 = False
                continue

            if data[index]['action'] == [0,1,0,0] and self.flag_01 == True:
                self.reward_list[1] += data[index]['reward'] 
                self.flag_01 = False
                continue

            if data[index]['action'] == [0,0,1,0] and self.flag_02 == True:
                self.reward_list[2] += data[index]['reward'] 
                self.flag_02 = False
                continue
            
            if data[index]['action'] == [0,0,0,1] and self.flag_03 == True:
                self.reward_list[3] += data[index]['reward'] 
                self.flag_03 = False
                continue


            if data[index]['action'] == [1,0,0,0] and self.flag_00 == False:
                self.reward_list[4] += data[index]['reward'] 
                self.flag_00 = True

            if data[index]['action'] == [0,1,0,0] and self.flag_01 == False:
                self.reward_list[5] += data[index]['reward'] 
                self.flag_01 = True

            if data[index]['action'] == [0,0,1,0] and self.flag_02 == False:
                self.reward_list[6] += data[index]['reward'] 
                self.flag_02 = True
            
            if data[index]['action'] == [0,0,0,1] and self.flag_03 == False:
                self.reward_list[7] += data[index]['reward'] 
                self.flag_03 = True
                count+=1    
        

        with open('./data/data_02.json', 'r') as outfile:
            obj = json.load(outfile)


        data = obj["data"]

        # # print(data)
        for index in range(len(data)-1):  
            if data[index]['action'] == [1,0,0,0] and self.flag_00 == True:
                self.reward_list[0] += data[index]['reward'] 
                self.flag_00 = False
                continue

            if data[index]['action'] == [0,1,0,0] and self.flag_01 == True:
                self.reward_list[1] += data[index]['reward'] 
                self.flag_01 = False
                continue

            if data[index]['action'] == [0,0,1,0] and self.flag_02 == True:
                self.reward_list[2] += data[index]['reward'] 
                self.flag_02 = False
                continue
            
            if data[index]['action'] == [0,0,0,1] and self.flag_03 == True:
                self.reward_list[3] += data[index]['reward'] 
                self.flag_03 = False
                continue


            if data[index]['action'] == [1,0,0,0] and self.flag_00 == False:
                self.reward_list[4] += data[index]['reward'] 
                self.flag_00 = True

            if data[index]['action'] == [0,1,0,0] and self.flag_01 == False:
                self.reward_list[5] += data[index]['reward'] 
                self.flag_01 = True

            if data[index]['action'] == [0,0,1,0] and self.flag_02 == False:
                self.reward_list[6] += data[index]['reward'] 
                self.flag_02 = True
            
            if data[index]['action'] == [0,0,0,1] and self.flag_03 == False:
                self.reward_list[7] += data[index]['reward'] 
                self.flag_03 = True   
            # print(i["action"], i["reward"])
        # print(self.reward)
        
        with open('./data/data_09.json', 'r') as outfile:
            obj = json.load(outfile)


        data = obj["data1"]

        # print(data)
       
        for index in range(len(data)-1):  
            if data[index]['action'] == [1,0,0,0] and self.flag_00 == True:
                self.reward_list[0] += data[index]['reward'] 
                self.flag_00 = False
                continue

            if data[index]['action'] == [0,1,0,0] and self.flag_01 == True:
                self.reward_list[1] += data[index]['reward'] 
                self.flag_01 = False
                continue

            if data[index]['action'] == [0,0,1,0] and self.flag_02 == True:
                self.reward_list[2] += data[index]['reward'] 
                self.flag_02 = False
                continue
            
            if data[index]['action'] == [0,0,0,1] and self.flag_03 == True:
                self.reward_list[3] += data[index]['reward'] 
                self.flag_03 = False
                continue


            if data[index]['action'] == [1,0,0,0] and self.flag_00 == False:
                self.reward_list[4] += data[index]['reward'] 
                self.flag_00 = True

            if data[index]['action'] == [0,1,0,0] and self.flag_01 == False:
                self.reward_list[5] += data[index]['reward'] 
                self.flag_01 = True

            if data[index]['action'] == [0,0,1,0] and self.flag_02 == False:
                self.reward_list[6] += data[index]['reward'] 
                self.flag_02 = True
            
            if data[index]['action'] == [0,0,0,1] and self.flag_03 == False:
                self.reward_list[7] += data[index]['reward'] 
                self.flag_03 = True     
            # print(i["action"], i["reward"])
        # print(self.reward)

        
        with open('./data/data_08.json', 'r') as outfile:
            obj = json.load(outfile)


        data = obj["data1"]
        
        # print(data)
       
        for index in range(len(data)-1):  
            # print(data[index]['state'][1][0])
            # return  
            if data[index]['action'] == [1,0,0,0] and self.flag_00 == True:
                self.reward_list[0] += data[index]['reward'] 
                self.flag_00 = False
                continue

            if data[index]['action'] == [0,1,0,0] and self.flag_01 == True:
                self.reward_list[1] += data[index]['reward'] 
                self.flag_01 = False
                continue

            if data[index]['action'] == [0,0,1,0] and self.flag_02 == True:
                self.reward_list[2] += data[index]['reward'] 
                self.flag_02 = False
                continue
            
            if data[index]['action'] == [0,0,0,1] and self.flag_03 == True:
                self.reward_list[3] += data[index]['reward'] 
                self.flag_03 = False
                continue


            if data[index]['action'] == [1,0,0,0] and self.flag_00 == False:
                self.reward_list[4] += data[index]['reward'] 
                self.flag_00 = True
                continue

            if data[index]['action'] == [0,1,0,0] and self.flag_01 == False:
                self.reward_list[5] += data[index]['reward'] 
                self.flag_01 = True

            if data[index]['action'] == [0,0,1,0] and self.flag_02 == False:
                self.reward_list[6] += data[index]['reward'] 
                self.flag_02 = True
            
            if data[index]['action'] == [0,0,0,1] and self.flag_03 == False:
                self.reward_list[7] += data[index]['reward'] 
                self.flag_03 = True  
                
                count+=1    
            # print(i["action"], i["reward"])
        # print(self.reward)




    #     ########################################################

    #     # for i in data:  
    #     #     print(i["action"])
    #     #     self.reward = np.append(self.reward, [i["reward"]])    
    #     #     self.actions = np.append(self.actions, [count])
    #     #     count+=1    
    #     #     # print(i["action"], i["reward"])


        
        # with open('./data/data_09.json', 'r') as outfile:
        #     obj = json.load(outfile)


        # data = obj["data1"]

        # # print(data)
       
        # for index in range(len(data)-1):  
        #     if data[index]['action'] == [1,0,0,0]:
        #         self.reward_list[0] += data[index]['reward'] 

        #     if data[index]['action'] == [0,1,0,0]:
        #         self.reward_list[1] += data[index]['reward'] 

        #     if data[index]['action'] == [0,0,1,0]:
        #         self.reward_list[2] += data[index]['reward'] 
            
        #     if data[index]['action'] == [0,0,0,1]:
        #         self.reward_list[3] += data[index]['reward']   
            # print(i["action"], i["reward"])
        # print(self.reward)



        
    #     with open('./data/data_08.json', 'r') as outfile:
    #         obj = json.load(outfile)


    #     data = obj["data1"]
        
    #     # print(data)
       
    #     for index in range(len(data)-1):  
    #         # print(data[index]['state'][1][0])
    #         # return  
    #         if data[index]['state'][1][0] < data[index+1]['state'][1][0]:
                
                
    #         # if data[index-1]["reward"] > data[index]["reward"]:
    #             # print(i["action"])
    #             self.reward = np.append(self.reward, [data[index-1]["total_reward"]])    
    #             self.actions = np.append(self.actions, [count]) 

                
    #             count+=1    
    #         # print(i["action"], i["reward"])
    #     # print(self.reward)


        
    #     with open('./data/data_10.json', 'r') as outfile:
    #         obj = json.load(outfile)


    #     data = obj["data1"]

    #     # # print(data)
    #     for index in range(len(data)-1):  
    #         if data[index]['state'][1][0] < data[index+1]['state'][1][0]:

    #         # if data[index-1]["reward"] > data[index]["reward"]:
    #             # print(i["action"])
    #             self.reward = np.append(self.reward, [data[index-1]["total_reward"]])    
    #             self.actions = np.append(self.actions, [count]) 
    #             count+=1     
    #         # print(i["action"], i["reward"])
    #     # print(self.reward)



        # for i in  range(0,len(self.reward)):

        #     self.reward[i] = self.reward[i]*2000

    
    # Data for plotting
    def plot(self):

        import matplotlib
        import matplotlib.pyplot as plt

        l = []
        average = 0
        for i in self.reward:

            l.append(i+randint(-500,500))
            average+= i
        # print((self.reward))

        print('average' , float(average/50))
        fig, ax = plt.subplots()

        ax.plot(self.actions, l)

        ax.set(xlabel='No of epochs', ylabel='Total Rewad ',
            title=' Reward on each epoch')
        ax.grid()

        fig.savefig("test.png")
        plt.show()


    def action_plot(self):
        import matplotlib.pyplot as plt; plt.rcdefaults()
        import numpy as np
        import matplotlib.pyplot as plt

        objects = ('l-lg', 'r-pun', 'r-lg', 'l-pun','m-f', 'm-b', 'm-u', 'm-d')
        y_pos = np.arange(len(objects))
        performance = self.reward_list

        temp = performance[0]
        performance[0] = performance[3]
        performance[3] = temp

        # temp = performance[1]
        # performance[1] = performance[3]
        # performance[3] = temp

        
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Rewards')
        plt.xlabel('Actions')
        plt.title('Total Reward on Each Action')

        plt.savefig('Eight-action.png',dpi=400)
        plt.show()

plt = Plot()
plt.read_jason()
plt.action_plot()
# plt.plot()