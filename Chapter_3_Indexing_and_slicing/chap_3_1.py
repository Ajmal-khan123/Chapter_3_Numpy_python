#__ very important for analysis

# _________/\________________/\_______________________/\___________

#__first we will define indexing=> (Selecting single element from array)
#  Fancy indexing : using a list of index to select multiple element

# _________/\________________/\_______________________/\___________

#__first we will define Slicing=> (Selecting multiple element from array )
# There are three parameter in the slicing 
# 1) __Start  2) __Stop  3) __Step

# _________/\________________/\_______________________/\___________

# Boolean Masking  : To check certain condition then filter the element .
# E.g:  Bol_mas=[1,2,3,4,5]
# Certain condition mean print those value which are less than 4  result=1,2,3

# _________/\________________/\_______________________/\___________

import numpy as np

# +ive,-ive  index 
arr=np.array([1,2,3,4,5])
# print(arr[0])

# Result=1

# _________/\________________/\_______________________/\___________
# print(arr[-2])
# print([arr[-3]]) #__when we used double square bracket then it will return also the type of data

# _________/\________________/\_______________________/\___________

#___Slicing 
arr_2=np.array([2,3,4,6,7,8,9,10,11,12,13,15,14,16])

# print(arr_2[0])  #_Result=> 2
# print(arr_2[0:4])   #_Result=> 2,3,4,6
# print(arr_2[-2:-1])  #_Result=> 14

# _________/\________________/\_______________________/\___________

#___Fancy Indexing 
# __Selecting multiple index at ones


f_array=np.array([2,3,4,5,6,7,8,9])
print(f_array[[2,3,1]])  # Result:=> 4,5,2
#  You will get those element for which you have index in the print function

print(f_array[[1,2,3]])  #  Result:=> 3,4,5

# _________/\________________/\_______________________/\___________

#___Final topic 
#___Filtering Data

Data=np.array([2,3,4,5,6,8,10])
print(Data[Data<=6])  # Result is 2,3,4,5,6 
