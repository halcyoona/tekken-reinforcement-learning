# from keysClass import *
import random


class pressKey():
    

    def buttonPress(self,button):
        keys = Keys()
        keys.directKey(button)
        sleep(0.1)
        keys.directKey(button, keys.key_release)
        sleep(0.7)


class KingCombos():

    def sample(self):
        keys = Keys()

        keys.directKey("a")
        sleep(0.1)
        keys.directKey("a", keys.key_release)

        keys.directKey("s")
        sleep(0.05)
        keys.directKey("s", keys.key_release)

        keys.directKey("a")
        sleep(0.05)
        keys.directKey("a", keys.key_release)
        sleep(0.5)

        keys.directKey("a")
        sleep(0.05)
        keys.directKey("a", keys.key_release)

class paulCombos:
    def samllCombo(self):
        keys = Keys()

        keys.directKey("a")
        sleep(0.2)
        keys.directKey("a", keys.key_release)

        keys.directKey("s")
        sleep(0.1)
        keys.directKey("s", keys.key_release)
        # sleep(0.1)

        keys.directKey("z")
        sleep(0.2)
        keys.directKey("z", keys.key_release)
        
        # sleep(0.4)
        keys.directKey("a")
        sleep(0.1)
        keys.directKey("a", keys.key_release)
        
        sleep(0.3)

        keys.directKey("s")
        sleep(0.1)
        keys.directKey("s", keys.key_release)

    def ultraInstantCombos(self):

        keys = Keys()

        keys.directKey("a")
        sleep(0.2)
        keys.directKey("a", keys.key_release)

        keys.directKey("s")
        sleep(0.1)
        keys.directKey("s", keys.key_release)
        # sleep(0.1)

        keys.directKey("z")
        sleep(0.2)
        keys.directKey("z", keys.key_release)
        
        # sleep(0.4)
        keys.directKey("a")
        sleep(0.1)
        keys.directKey("a", keys.key_release)
        
        sleep(0.5)
        keys.directKey("x")
        sleep(0.1)
        keys.directKey("x", keys.key_release)

        sleep(0.3)
        keys.directKey("s")
        sleep(0.1)
        keys.directKey("s", keys.key_release)

        sleep(0.2)
        keys.directKey("a")
        sleep(0.1)
        keys.directKey("a", keys.key_release)

        sleep(0.2)
        keys.directKey("x")
        sleep(0.1)
        keys.directKey("x", keys.key_release)

        sleep(0.2)
        keys.directKey("s")
        sleep(0.1)
        keys.directKey("s", keys.key_release)

        sleep(0.2)
        keys.directKey("a")
        sleep(0.1)
        keys.directKey("a", keys.key_release)

    def stepForwards(self, steps):
        keys = Keys()
        i = 0
        for i in range(0,steps):
            sleep(0.2)
            keys.directKey("l")
            sleep(0.1)
            keys.directKey("l", keys.key_release)

    def twoPunch(self):
        keys = Keys()
        sleep(0.2)
        keys.directKey("j")
        # sleep(0.1)

        keys.directKey("a")
        sleep(0.1)
        
        keys.directKey("a", keys.key_release)
        sleep(0.1) 

        keys.directKey("s")
        sleep(0.1)
        keys.directKey("s", keys.key_release)

        keys.directKey("j", keys.key_release)

    def randonAction(self):
        actionList = ["a","s","z","x","j","k","l","i","twoPunch","ultraInstantCombos","samllCombo"]
        
        i = 0
        for i in range(0,200):
            action = random.choice(actionList)
            if action == "twoPunch":
                self.twoPunch()
            if action == "ultraInstantCombos":
                self.ultraInstantCombos()
            if action == "samllCombo":
                self.samllCombo()
            keys = Keys()

            keys.directKey(action)
            sleep(0.2)
            keys.directKey(action, keys.key_release)

            sleep(0.5)
            i += 1
        



    

if __name__ == '__main__':
    sleep(3)
    # comb = KingCombos()
    # comb.sample()

    # paul = paulCombos()
    # paul.samllCombo()
    # sleep(1)
    
    # paul.stepForwards(5)
    # sleep(1)

    #paul.ultraInstantCombos()

    # paul.stepForwards(10)
    # paul.twoPunch()

    # paul.stepForwards(2)
    # paul.twoPunch()

    # sleep(1)
    # paul.stepForwards(2)
    # paul.twoPunch()


    # sleep(1)

    # paul.ultraInstantCombos()

    #paul.randonAction()

    button = pressKey()
    button.buttonPress("a")
    button.buttonPress("z")
    button.buttonPress("x")
    button.buttonPress("x")
    button.buttonPress("x")


