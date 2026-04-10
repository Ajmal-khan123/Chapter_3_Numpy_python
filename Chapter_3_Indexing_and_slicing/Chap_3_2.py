# _________/\________________/\_______________________/\___________

#___Reshaping and Manipulating array

#  Definition :  Changing dimension without modifying data
# From one dimension to 2 dimension or 3 dimension
# If dimension match then reshaping can be occur other wise not
# Element maintenance is must

## _________/\________________/\_______________________/\___________
import numpy as np

# arr_Dim=np.array([1,2,3,4,5,6])

# Here it is possible the array can convert from single _D to 2_ Dimensional
# if element is [1,2,3,4,5] then it is not convert into two Dimensional

# print(arr_Dim.reshape(3,2))

# ____/\___
# Result

# e" "c:/Users/Nabil_Ajmal khan/OneDrive/Desktop/Numpy/Chapter_3_Indexing_and_slicing/Chap_3_2.py"
# [[1 2]
#  [3 4]
#  [5 6]]

# print(arr_Dim.reshape(2,3))

# ____/\___
# Result
# [[1 2 3]
#  [4 5 6]]

# _________/\________________/\_______________________/\___________

#  Flattening Array
# To change multi dimensional array into single array
# 1) Ravel: Return view
# 2) Flatten : Return  copy

Flat_Array=np.array([[1,2,3],[3,4,5]])
print(Flat_Array.ravel())
print("check the difference")
print(Flat_Array.flatten())

# _Resulted array is=[1,2,3,4,5,6]

# Summary! 
# 1) Indexing  Flatten
# 2) Indexing slicing
# 3) Fancy Indexing 
# 4) Boolean Masking
# 5) Array Shape