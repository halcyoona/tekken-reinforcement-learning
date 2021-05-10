import time
from dqn_learning_tf1 import Enviroment
import pyautogui
import mss
import numpy
from PIL import ImageGrab
import keyboard
import cv2
import json

class ScreenCapture:
    def __init__(self):
        # title of our window
        self.title = "FPS benchmark"
        
        # set start time to current time
        self.start_time = time.time()
        
        #set end time accordingly
        self.end_time = self.start_time + 300
        
        # displays the frame rate every 2 second
        self.display_time = 2
        
        # Set primarry FPS to 0
        self.fps = 0
        
        # Load mss library as sct
        self.sct = mss.mss()
        
        # Set monitor size to capture to MSS
        self.monitor = {"top": 40, "left": 0, "width": 800, "height": 640}
        
        # Set monitor size to capture Gap PC
        # self.mon = (0, 0, 1920, 1080)
        # Bashir PC
        self.mon = (0, 0, 1280, 720)


    def screenRecordPIL(self):
        
        state = [[100,100], [60,0]]
        reward = 0
        done = False

        TIME = time.time() - self.start_time 
        # begin our loop
        total_reward = 0
        data = {}
        count = 1
        data['data'+str(count)] = []

        env = Enviroment()

        
        flag = 0
        while self.start_time < self.end_time:

            TIME =  time.time() - self.start_time

            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.asarray(ImageGrab.grab(bbox=self.mon))
            
            # to ger real color we do this:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
            cv2.imwrite("./pictures/tekken-7-4k.png", img, [cv2.IMWRITE_JPEG_QUALITY, 50])
            # Display the picture
            # cv2.imshow(self.title, img)
            
            values = env.enviromnet(state, done, (60 - TIME))

            state = values[2]
            total_reward += values[3]
            done = values[4]
            
            data['data'+str(count)].append({
                'state': values[0],
                'action': values[1],
                'next_state': values[2],
                'reward': values[3],
                'done': values[4],
                'total_reward': total_reward

            })
            
            if state[0][0] == 0 or state[0][1] == 0:
                total_reward = 0
                done = True
                self.start_time = time.time()
                TIME = time.time() - self.start_time  
                state = [[100,100], [60 - TIME,0]]
            
            if TIME > 60:
                total_reward = 0
                done = True
                self.start_time = time.time()
                TIME = time.time() - self.start_time  
                state = [[100,100], [60 - TIME,0]]
            

            if keyboard.is_pressed('p'):
                pause= True

                flag = 1
                # file = './data/data_08.json'
                # with open(file , 'w') as outfile:
                #     json.dump(data, outfile)
                
                print("Pause")
                # env.training(file, count)
                # count += 1
                # data['data'+str(count)] = []
                while(pause):
                    if keyboard.is_pressed('r'):
                        pause = False
                        print("Start")
        
           

            # add one to fps
            self.fps+=1
            # calculate time difference
            TIME = time.time() - self.start_time
            
            # this If statement is to check FPS when display time is passed
            if (TIME) >= self.display_time :
                print("FPS: ", self.fps / (TIME))
                print("No of data counts : ", count)
                # set fps again to zero
                self.fps = 0
                # set start time to current time again
                
        file = './data/data_10.json'
        with open(file , 'w') as outfile:
            json.dump(data, outfile)
        
        
        env.training(file, count)

        # with open("./data/data_01.txt", 'a') as f:
        #     for i in lst:
        #         f.write(i)
       

if __name__ == '__main__':

    obj = ScreenCapture()
    obj.screenRecordPIL()
