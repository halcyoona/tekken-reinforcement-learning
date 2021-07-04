import tensorflow as tf
from tensorflow.keras import layers, models


class CNN():
    def __init__(self, state_dim, learning_rate, discount_rate, epsilon):
        
        self.network = models.Sequential()
        self.network.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=state_dim))
        self.network.add(layers.MaxPooling2D((2, 2)))
        self.network.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.network.add(layers.MaxPooling2D((2, 2)))
        self.network.add(layers.Conv2D(128, (3, 3), activation='relu'))
        self.network.add(layers.Flatten())
        self.network.add(layers.Dense(64, activation='relu'))
        self.network.add(layers.Dense(1, activation="linear"))
        self.optimizer = self.network.optimizers.RMSprop(lr=learning_rate, rho=discount_rate, epsilon=epsilon)
        self.network.compile(self.optimizer, loss='mse')


    def updateModel(self, state, reward):
        self.network.fit(state, reward)
    

    def getReward(self, state):
        return self.network.predict(state)

    
    def saveModel(self):
        self.network.save_weights("./save_models/reward_weights.h5")

    def loadModel(self):
        self.network.load_weights("./save_models/reward_weights.h5")

    def modelSummary(self):
        self.network.summary()



# if __name__ == '__main__':
#     ins = DDQNetwork((1280, 720, 3), 8, learning_rate=0.01, discount_rate=0.97,  epsilon=1.0)
#     ins.model_summary()