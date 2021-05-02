import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import json

def read_jason():
    with open('./data/data_04.json', 'r') as outfile:
        obj = json.load(outfile)


    data = obj["data1"]
    print(data)

    for i in data:      
        print(i["action"], i["total_reward"])
# Data for plotting
def plot():
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='About as simple as it gets, folks')
    ax.grid()

    fig.savefig("test.png")
    plt.show()

read_jason()