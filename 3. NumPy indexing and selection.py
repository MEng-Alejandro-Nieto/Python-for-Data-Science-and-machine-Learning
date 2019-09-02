import numpy as np 


arr=np.arange(10)
print(arr)
print(arr[8])			# Indexing
print(arr[2:8])			# Slicing from index  untiltill (exclusive)
print(arr[:5])
#----------------------------------------------------------------
print("Block 2\n")
arr[4:]=100				# it changes the value from index 4(exclusive) o the end 
print(arr)

print("\n")
#----------------------------------------------------------------
print("Block 2\n")
arr=np.arange(11)
slice_of_arr=arr[0:6]		# this makes the fisrt 6 index equl to slice_of_arr and the other way around
print(slice_of_arr)
slice_of_arr[:]=99
print(slice_of_arr)			# it ill show the first 6 index equal to 99 
print(arr)					# it ill show the first 6 index equal to 99

print("\n")
#----------------------------------------------------------------
print("Block 3\n")
arr_copy=arr.copy()

print(arr)
print(arr_copy)
arr[0:6]=np.arange(0,6)
print(arr)
print(arr_copy)

print("\n")


#----------------------------------------------------------------
print("Block 4\n")
print("INDEXING OF A 2D ARRAY 'MATRIX'")
arr_2d=np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
print(arr_2d[0][2])			# double bracket notation
print(arr_2d[0,2])			# comma single bracket notation

print(arr_2d[0])
print(arr_2d[1])


print("\n")


#----------------------------------------------------------------
print("Block 5\n")
print("SLICING OF A 2D ARRAY 'MATRIX'")

print(arr_2d[:2,1:])
print(arr_2d[1:2,0:])
print(arr_2d[:,2:])
print("\n")


#----------------------------------------------------------------
print("Block 6\n")
print("CONDITIONAL SELECTION 'MATRIX'")

print(arr>5)			# it print boolean values of the index values based on the condition
print(arr[arr>5])		# it will print only the numbers that satisfy the condition
print(arr[arr<=3])

print("\n")

#----------------------------------------------------------------
print("Block 7\n")
arr=np.arange(50).reshape(5,10)
print(arr)

print("")
print(arr[1:4,3:7])
print("")
print(arr[0:1,2:7])
print("")
print(arr[:,7:8])


print("\n")
#----------------------------------------------------------------
print("Block 8\n")

print("\n")


#----------------------------------------------------------------
print("Block 9\n")

print("\n")


#----------------------------------------------------------------
print("Block 10\n")

print("\n")


#----------------------------------------------------------------


