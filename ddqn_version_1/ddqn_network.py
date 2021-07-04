import tensorflow as tf
from tensorflow.keras import layers, models



class DDQNetwork():
    def __init__(self, state_dim, action_size, learning_rate, discount_rate, epsilon):
        
        self.network = models.Sequential()
        self.network.add(layers.Conv2D(32, kernel_size=(3,3),   activation='relu', input_shape=state_dim))
        print( self.network.input_shape)
        # self.network.add(layers.MaxPooling2D((2, 2)))
        self.network.add(layers.Conv2D(64, kernel_size=(3,3), activation='relu'))
        # self.network.add(layers.MaxPooling2D((2, 2)))
        self.network.add(layers.Conv2D(128, kernel_size=(3,3), activation='relu'))
        self.network.add(layers.Flatten())
        self.network.add(layers.Dense(64, activation='relu'))
        self.network.add(layers.Dense(8, activation="linear"))
        self.optimizer = tf.keras.optimizers.RMSprop(name='RMSprop',lr=learning_rate, rho=discount_rate, epsilon=epsilon)
        self.network.compile(self.optimizer, loss='mse')


    def updateModel(self, state, q_values):
        self.network.fit(state, q_values)
    

    def getQState(self, state):
        return self.network.predict(state)

    
    def saveModel(self):
        self.network.save_weights("./saved_model_q/weights.h5")

    def loadModel(self):
        self.network.load_weights("./saved_model_q/weights.h5")

    def modelSummary(self):
        self.network.summary()



if __name__ == '__main__':
    ins = DDQNetwork(( 64, 64, 1) , 8, learning_rate=0.01, discount_rate=0.97,  epsilon=1.0)
    ins.modelSummary()