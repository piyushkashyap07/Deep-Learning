import numpy as np 
import nnfs 
from nnfs.datasets import spiral_data

nnfs.init()
class Layer_Dense:
    def __init__(self, n_input, n_neuron):
        self.weights = np.random.randn(n_input, n_neuron)
        self.bias = np.random.randn(1, n_neuron)
        
    def forward(self, input):
        self.output= np.dot(input, self.weights)+self.bias

x,y=spiral_data(samples=100,classes=3)
dense1=Layer_Dense(2,3)
dense1.forward(x)
print(dense1.output[:5])