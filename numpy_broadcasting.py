# array summation
import numpy as np 
a=[[1,2,3],[4,5,6],[7,8,9]]
# b=np.reshape(3,3,-1)
obj_a =np.array(a)
print(obj_a.sum())
print(np.sum(obj_a, axis=None))
# print(np.sum(obj_a, axis=0))
print(np.sum(obj_a, axis=0,keepdims=True))
# print(np.sum(obj_a, axis=1))
print(np.sum(obj_a, axis=1,keepdims=True))

sub_with_max_row = a-np.max(a, axis=1, keepdims=True)
print(sub_with_max_row)


