
import time
from dqn_learning_tf1 import Enviroment
import pyautogui
import mss
import numpy
from PIL import ImageGrab
import keyboard
import cv2
import json

from keysclass import *

from PIL import Image
from pytesseract import pytesseract
 

class pressKey():
    

    def buttonPress(self,button):
        keys = Keys()
        keys.directKey(button)
        sleep(0.1)
        keys.directKey(button, keys.key_release)
        sleep(0.7)


    
    
import cv2

class TekkenAutomate :    
    def __init__(self):
        self.button = pressKey()
#         print(menue_screen_text)
    def checkMainManue(self,image_path):
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        img = Image.open(image_path)

        pytesseract.tesseract_cmd = path_to_tesseract

        text = pytesseract.image_to_string(img)

        menue_screen_text =  text.split()

        print(menue_screen_text)

        if 'News' in menue_screen_text or 'Change' in menue_screen_text or'Player' in menue_screen_text or'Replays' in menue_screen_text or 'Customization' in menue_screen_text or 'Gallery' in menue_screen_text or 'Options' in menue_screen_text  :
            print('yes')
            self.button.buttonPress('k')
            time.sleep(0.5)
            self.button.buttonPress('k')
            time.sleep(0.5)
            self.button.buttonPress('z')
            time.sleep(0.5)
            self.button.buttonPress('z')
            time.sleep(10)

            #select side always left

            self.button.buttonPress('z')
            time.sleep(2)
            
            #select ramdom character

            self.button.buttonPress('l')
            time.sleep(0.5)
            self.button.buttonPress('z')
            
tekken = TekkenAutomate()
tekken.checkMainManue(r"menue-image.jpg") 
class ScreenCapture:
    def __init__(self):

        #button object
        butten = pressKey()

        ######################################automation code
        #tekken automate flag 
        self.game_flage = True

        self.
        ###################################################
        # title of our window
        self.title = "FPS benchmark"
        
        # set start time to current time
        self.start_time = time.time()
        
        #set end time accordingly
        self.end_time = self.start_time + 200
        
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

        img = numpy.asarray(ImageGrab.grab(bbox=self.mon))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        while self.start_time < self.end_time:
            
            if self.game_flage == True: # its means you are not in game

            


            TIME =  time.time() - self.start_time

            # Get raw pixels from the screen, save it to a Numpy array
            next_img = numpy.asarray(ImageGrab.grab(bbox=self.mon))
            
            # to ger real color we do this:
            next_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
            cv2.imwrite("./pictures/tekken-7-4k.png", next_img, [cv2.IMWRITE_JPEG_QUALITY, 50])
            # Display the picture
            # cv2.imshow(self.title, img)
            
            values = env.enviromnet(state, done, (60 - TIME), img)

            state = values[2]
            total_reward += values[3]
            done = values[4]
            
            
            data['data'+str(count)].append({
                'state': img,
                'action': values[1],
                'next_state': next_img,
                'reward': values[3],
                'done': values[4],
                'total_reward': total_reward

            })

            img = next_img
            
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

                
                
                with open('./data/data_01.json', 'w') as outfile:
                    json.dump(data, outfile)
                
                print("Pause")
                # env.training(count)
                return
                count += 1
                data['data'+str(count)] = []
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

       

if __name__ == '__main__':

    obj = ScreenCapture()
    obj.screenRecordPIL()
