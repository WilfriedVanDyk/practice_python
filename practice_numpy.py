# a numpy array must be of the type of float!!!!! (no other or mixed types!! in the array)
import numpy as np
# Constructing an array with a simple list results in a 1d array
array1 = np.array([10, 100, 1000.])
# Constructing an array with a nested list results in a 2d array
array2 = np.array([[1., 2., 3.],
                   [4., 5., 6.]])

# print(array2.dtype)
# to change datatype (of python) to dtype of numpy (in this case float)
float(array1[0])

# vectorization
array1 += 1
# print(array1)
array1 -= 1

# broadcasting (If you use two arrays with different shapes in an arithmetic operation,
# NumPy extends—if possible—the smaller array automatically across the larger array so that
# their shapes become compatible
# print(array1 * array2)
# print(array2 * array1)
# print (array2 * array2)

# To perform matrix multiplications or dot products, use the @ operator
array2 @ array2.T  # array2.T is a shortcut for array2.transpose()
"""
Out[11]: array([[14., 32.],
                [32., 77.]])
"""
#  UFUNct
np.sqrt(array2)

# Some of NumPy’s ufuncs, like sum, are additionally available as array methods:
# if you want the sum of each column, do the following:
u = array2.sum(axis=0)  # Returns a 1d array (sum along vertical axis)
v = array2.sum(axis=1)  # horizontal axis (axis = 0)
w = array2.sum()  # sum of all elements
# print("array", u, v)

# selecting an element of the matrix, or by slicing getting diff fields
# numpy_array[row_selection, column_selection]
array2[0, 0]
array2[:, 1:]
array2[1, :2]

# arange gives an array of 12 elements, and reshapes it into a matrix
u = np.arange(12).reshape(4,3)
# print(u)

# random / np.ones or zeros / np.eye to create the identy matrix
v = np.random.randn(2,3)
print(v)

# view (changes the original) and copy (no change on the original)
array2 = np.array([[1., 2., 3.],
                [4., 5., 6.]])
subset = array2[:, :2]
subset[0, 0] = 1000
# Out[29] array2: array([[1000., 2., 3.], [4., 5., 6.]])
# if you want no change of the original: working an a copy!!!
subset.array2[:,:2].copy()
