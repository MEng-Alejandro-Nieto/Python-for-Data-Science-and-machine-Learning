import numpy as np
'''
* we can sum A+B matrices if and only if they have the same size
* we can multiply A*B if and only if the number of columns of the left matrix is the same as the number of rows of the right matrix

'''

#--------------------------------------
print("-----------------------------------------")
print("Block 1")
A=np.arange(0,11)
B=np.arange(10,21)
print(A)
print(B)

print("-----------------------------------------")
print("Block 2 ")
print(A+B)
print(A*B)
print(A+100)		# add 100 to each element of A
print(A-100)		# rest 100 to each element of A
print(A*100)		# scalar Multiplication
print(A/100)		# scalar division
print(A**2)			# each element of A to the power of 2

print("-----------------------------------------")
print("Block 3")
print(A**0.5)		# square root of each element of A
print(np.sqrt(A))	# square root of each element of A

print("-----------------------------------------")
print("Block 4")
print(np.exp(A))	# exponential of each element of A


print("-----------------------------------------")
print("Block 5")

print(np.max(A))


print("-----------------------------------------")
print("Block 6")

print(np.sin(A))		# it will return the sin() of each element of A in Radians
print(np.log(A))		# ir will take log of each element of A 

print("-----------------------------------------")
