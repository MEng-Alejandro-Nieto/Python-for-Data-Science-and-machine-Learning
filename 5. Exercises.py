'''
1. Create anrray of 10 zeros
2. Create an array of 10 ones
3. Create an array of 10 fives
4. Create and array of the integers from 10 to 50
5. Create an array of all thee even integers from 10 to 50
6. Create a 3x3 matrix with values ranging from 0 to 8
7. Create a 3x3 identity matrix
8. Use NumPy to generate a random number between 0 and 1
9. Use NumPy to generate an array of 25 random numbers from a standart normal distribution
10. Create a 2D matrix of [10x10] with thee folowing order [0.01 0.02..]
11. Create an array of 20 linearly spaced points between 0 and 1

'''
import numpy as np

print("------------------------------------------------------")

print("Answer 1")
a=np.zeros(10)
print(a)

print("------------------------------------------------------")

print("Answer 2")
b=np.ones(10)
print(b)

print("------------------------------------------------------")

print("Answer 3")
c=5*b
print(c)

print("------------------------------------------------------")

print("Answer 4")
d=np.arange(10,51)
print(d)




print("------------------------------------------------------")

print("Answer 5")
e=np.arange(10,51,2)
print(e)


print("------------------------------------------------------")

print("Answer 6")
f=np.arange(0,9).reshape(3,3)
print(f)

print("------------------------------------------------------")
print("Answer 7")

g=np.eye(3)
print(g)


print("------------------------------------------------------")
print("Answer 8")

h=np.random.rand(1)
print(h)

print("------------------------------------------------------")
print("Answer 9")

i=np.random.randn(25)
print(i)

print("------------------------------------------------------")
print("Answer 10")

j=np.arange(0.1,10.1,0.1).reshape(10,10)	# or
j=np.linspace(0.01,1,100).reshape(10,10)
print(j)

print("------------------------------------------------------")
print("Answer 11")

k=np.linspace(0,1,20)
print(k)

print("------------------------------------------------------")
print("Answer 12")
l=np.arange(1,26).reshape(5,5)
print(l)
print("\n")
print(l[2:,1:])

print("------------------------------------------------------")
print("Answer 13")

print(l[3,4])


print("------------------------------------------------------")
print("Answer 14")

print(l[:3,1:2])

print("------------------------------------------------------")
print("Answer 15")

print(l[4:,:])

print("------------------------------------------------------")
print("Answer 16")

print(l[3:,:])

print("------------------------------------------------------")
print("Answer 17")


print(np.sum(l))		#  or
print(l.sum())

print("------------------------------------------------------")
print("Answer 18")
# standard deviation
print(np.std(l))		# or
print(l.std())

print("------------------------------------------------------")
print("Answer 19")
# get the sums of all columns in 'l'
print(l.sum(axis=0))







