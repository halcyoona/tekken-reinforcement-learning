import tensorflow as tf
from tensorflow.keras import layers, models


class DDQNetwork():
    def __init__(self, state_dim, action_size, learning_rate, discount_rate, epsilon):
        
        self.network = models.Sequential()
        self.network.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=state_dim))
        self.network.add(layers.MaxPooling2D((2, 2)))
        self.network.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.network.add(layers.MaxPooling2D((2, 2)))
        self.network.add(layers.Conv2D(128, (3, 3), activation='relu'))
        self.network.add(layers.Flatten())
        self.network.add(layers.Dense(64, activation='relu'))
        self.network.add(layers.Dense(action_size, activation="linear"))
        self.optimizer = self.network.optimizer.RMSprop(name='RMSprop',lr=learning_rate, rho=discount_rate, epsilon=epsilon)
        self.network.compile(self.optimizer, loss='mse')


    def update_model(self, state, q_values):
        self.network.fit(state, q_values)
    

    def get_q_state(self, state):
        return self.network.predict(state)

    
    def save_model(self):
        self.network.save_weights("./save_models/weights.h5")

    def load_model(self):
        self.network.load_weights("./save_models/weights.h5")

    def model_summary(self):
        self.network.summary()



if __name__ == '__main__':
    ins = DDQNetwork((1280, 720, 3), 8, learning_rate=0.01, discount_rate=0.97,  epsilon=1.0)
    ins.model_summary()