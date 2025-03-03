import numpy as np 

input=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

weights=[
    [0.1,0.2,0.3,0.4],
    [0.1,0.2,0.3,0.4],
    [0.1,0.2,0.3,0.4]
]

bias = [2,3,0.5]

weight2=[
    [0.1, 0.34, 0.34],  # ✅ Fixed comma issue
    [0.21, 0.14, 0.30],
    [0.12, 0.84, 0.34]
]

bias2=[-1,2,-0.5]

input_array = np.array(input)
weight1_array = np.array(weights)
weight2_array = np.array(weight2)
bias_array = np.array(bias)
bias2_array = np.array(bias2)

layer_output_1 = np.dot(input_array, weight1_array.T) + bias_array
layer_output_2 = np.dot(layer_output_1, weight2_array.T) + bias2_array

print(layer_output_1)
print(layer_output_2)
