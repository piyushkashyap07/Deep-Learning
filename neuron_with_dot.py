# using dot product

import numpy as np 
inputs = [1.0, 2.0, 3.0,2.5]
weights = [0.2,0.8,-0.5,1.0]
bias =2.0

output = np.dot(inputs, weights)+bias
output2 = np.dot(weights,inputs)+bias
print(output)
print(output2)


# layer
input=[1.0,2.0,3.0,4.0]
weight=[[0.2,0.8,-0.5,1],
        [0.5,-0.91,0.26,-0.5],
        [-0.26,-0.27,0.17,0.87]]

biases=[2.0,3.0,0.5]

output3=np.dot(weight, input)+biases
print(output3)

# transpose

input=[
    [1.0,2.0,3.0,2.5],
    [2.0,5.0,-1.0,2.0],
    [-1.5,2.7,3.3,-0.8]
]
weight=[
    [0.2,0.8,-0.5,1],
    [0.5,-0.91,0.26,-0.5],
    [-0.26,-0.27,0.17,0.87]
]

bias=[2.0,3.0,0.5]

output4=np.dot(input,np.array(weight).T)+bias
print(output4)