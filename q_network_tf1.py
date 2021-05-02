import tensorflow.compat.v1 as tf   
import numpy as np

class QNetwork():
    def __init__(self, state_dim, action_size, learning_rate):
        self.state_in = tf.placeholder(tf.float32, shape=[1, *state_dim])
        print(self.state_in.shape)
        self.action_in = tf.placeholder(tf.int32, shape=[1, *action_size])
        self.action_in_check = tf.placeholder(tf.int32, shape=[1])
        print(self.action_in.shape)
        print(self.action_in_check.shape)
        self.q_target_in = tf.placeholder(tf.float32, shape=[None])
        print(self.q_target_in.shape)
        action_one_hot = tf.one_hot(self.action_in_check, depth=action_size[1])
        print(action_one_hot.shape)
        
        self.hidden1 = tf.layers.dense(self.state_in, 100, activation=tf.nn.relu)
        print(self.hidden1.shape)
        self.q_state = tf.layers.dense(self.hidden1, 2, activation=None)
        print(self.q_state.shape)
        self.q_state_action = tf.reduce_sum(tf.multiply(self.q_state, action_one_hot), axis=0)          
        print(self.q_state_action.shape)
        self.loss = tf.reduce_mean(tf.square(self.q_state_action- self.q_target_in)) 
        self.optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(self.loss)
        return 
    def update_model(self, session, state, action, q_target):
        feed = {self.state_in:state, self.action_in:action, self.q_target_in:q_target}
        session.run(self.optimizer, feed_dict=feed)

    def get_q_state(self, session, state):
        q_state = session.run(self.q_state, feed_dict={self.state_in:state})
        return q_state
