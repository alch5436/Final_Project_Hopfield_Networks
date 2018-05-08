# Testing the Hopfield Network
# Import the class
import numpy as np
from Hopfield.py import Hopfield

# Create the network ~~~~~~~ YAY
my_network = Hopfield()

# Process Data Here ~~~~~~~ Whatever you want
'''
[[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0],
 [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]]
 '''
a = np.array([1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1])

# Use the network!
# my_network.learn(Whatever you wanna learn! :)
my_network.learn(a)
