'''
*NumPy is a linear algebra library for Pthon, the reason it is so 
 important for Data Science with python is that almost all of the 
 libraries in th PyData ecosystem rely on NumPy as one of ther main 
 building blocks

*NumPy is also incredibly fast, as it has bindings to C libraries

* NumPy arrays are the manin way we will use NumPY throughout the course

* Numpy arrays essentially come in two flavors: vectors and matrices

* vectors are strictly 1D arrays and matrices are 2D

'''

#-------------------------------------------------------------
print("Block 1\n")

my_list=[1,2,3]
print(my_list)

print("\n"*3)
#-------------------------------------------------------------

print("Block 2\n")

import numpy as np
print(np.array(my_list))


print("\n"*3)
#-------------------------------------------------------------
print("Block 3\n")

my_mat=[[1,2,3],[4,5,6],[7,8,9]]
print(f"this is a list: {my_mat}")
my_mat2=np.array(my_mat)
print(f"this is an array:\n{my_mat2}")

print("\n"*3)

#-------------------------------------------------------------
print("Block 4\n")

print(np.arange(0,10))
print(np.arange(0,10,2))

print(np.linspace(0,5,11))
print("\n"*3)

#-------------------------------------------------------------
print("Block 5\n")

print(np.zeros(5))
print("")
print(np.zeros((2,3)))
print("")
print(np.ones(5))
print("")
print(np.ones((3,4)))

print("\n"*3)


#-------------------------------------------------------------
print("Block 6\n")

print(np.eye(4))

print("\n"*3)


#-------------------------------------------------------------
print("Block 7\n")

print(np.random.rand(5))
print("")
print(np.random.rand(5,5))
print("")
print(np.random.randn(5))
print("")
print(np.random.randint(1,100))
print("")
print(np.random.randint(1,100,3))
print("\n"*3)


#-------------------------------------------------------------
print("Block 8\n")

arr=np.arange(50)					# 1D array from 0 to 25(exclusive)
print(arr)
print(arr.reshape(5,10))				# 2D array (5 rows and 5 columns)

print("\n"*3)


#-------------------------------------------------------------
print("Block 9\n")

ranarr=np.random.randint(0,100,5)	# random array
print(ranarr)
print(ranarr.max())
print(ranarr.argmax())
print(ranarr.argmin())

print("\n"*3)

