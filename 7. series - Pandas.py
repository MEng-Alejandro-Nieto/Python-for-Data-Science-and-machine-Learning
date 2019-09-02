# SERIES

import numpy as np
import pandas as pd
labels=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}
print("Block 1")
print("--------------------------------------------------")
print(labels)
print(my_data)
print(arr)
print(d)

print("--------------------------------------------------")
print("Block 2")
print(pd.Series(data=my_data))	# it will create a table that can be indexed via numbers
print(pd.Series(data=my_data,index=labels)) # it will create a table that can be indexed via numbers

print("--------------------------------------------------")
print("Block 3")
# VIA  A LIST
print("")
print(pd.Series(my_data,labels)) 	

print("--------------------------------------------------")
print("Block 4")
# VIA  A ARRAY
print("")
print(pd.Series(arr,labels)) 

print("--------------------------------------------------")
print("Block 5")
#VIA A DICTIONARY
print("")
print(pd.Series(d))	

print("--------------------------------------------------")
print("Block 6")
# VIA LABELS
print(pd.Series(labels))

print("--------------------------------------------------")
print("Block 7")
ser1=pd.Series([1,2,3,4],['USA','GERMANY','USSR', 'JAPAN'])
print(ser1)
ser2=pd.Series([1,2,3,4],['USA','GERMANY','ITALY','JAPAN'])
print("")
print(ser2['USA'])
print(ser2['GERMANY'])
print(ser2['ITALY'])
print(ser2['JAPAN'])

print("--------------------------------------------------")

print(ser1 +ser2)