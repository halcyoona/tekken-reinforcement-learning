import math
import random
class part_a:
    def __init__(self):
        self.x_minimum = 0
        self.x_maximum = 2
        self.num_steps = 1000000
        self.num_points = 1000000

    def function(self,x):
        return math.sqrt((math.cos(x) ** 2) + 1)

    def perform_experiment(self):
        y_minmum = self.function(self.x_minimum)
        y_maximum = y_minmum

        for i in range(self.num_steps):
            x = random.randint(0,2) 
            y = self.function(x)

            if y < y_minmum: 
                y_minmum = y
            if y > y_maximum: 
                y_maximum = y

        rect_area = (self.x_maximum - self.x_minimum) * (y_maximum - y_minmum)

        under_curve = 0

        for j in range(self.num_points):
            x = random.randint(0,2) 
            y = random.randint(y_minmum,y_maximum) 
            if self.function(x) > 0 and y > 0 and y <= self.function(x):
                under_curve += 1
            if self.function(x) < 0 and y < 0 and y >= self.function(x):
                under_curve += 1

        arera_under_the_curve = rect_area * float(under_curve) / self.num_points
        
        return arera_under_the_curve
obj = part_a()

print (" Area under the curve = " + str(obj.perform_experiment()))
