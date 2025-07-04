#Arrays in python can only contain elements of same data types i.e., data type of array should be homogeneous. It is a thin wrapper around C language arrays and consumes far less memory than lists.
#Lists in python can contain elements of different data types i.e., data type of lists can be heterogeneous. It has the disadvantage of consuming large memory.
#Arrays are mutable, meaning you can change the elements of an array after it has been created. Lists are also mutable, allowing you
# List are mutable, meaning you can change the elements of a list after it has been created. Arrays are also mutable, allowing you to modify their elements.
# However, arrays are more efficient for numerical operations and require less memory than lists.
# In Python, the array module provides a way to create arrays that are more memory-efficient than lists.

# Creating an array of integers
int_array=[1, 2, 3, 4,4, 0,5]
#length of the array
print(len(int_array))
# Accessing elements of the array
print(int_array[0])
print(int_array[-1])
# Slicing the array
print(int_array[2:4])
# Adding an element to the array
int_array.append(4)
print(int_array)
#sorting the array
int_array.sort()
print(int_array)
