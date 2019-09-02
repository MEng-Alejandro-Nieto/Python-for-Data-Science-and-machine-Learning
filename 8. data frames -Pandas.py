import numpy as np
import pandas as pd  

from numpy.random import randn,rand
np.random.seed(101)

print("--------------------------------------------------")
print("Block 1 (checking rand a randn)\n")

a=rand(2,3)
b=randn(2,3)
print(a)
print("")
print(b)
print("")
print(type(a))

print("--------------------------------------------------")
print("Block 2 (printing a Data Frame)\n")

df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

print("--------------------------------------------------")
print("Block 3 (Indexing columns)\n")

print(df['W'])
print(df[['X','W']])

print("--------------------------------------------------")
print("Block 4 (Indexing rows)")

print(df.loc['A'])		# indexing by row name
print("")
print(df.iloc[1])		# indexing by row position

print("--------------------------------------------------")
print("Block 5 (Creating new columns in data frames)\n")

df['new-1']= df['W']+df['X']
print(df)
df['new-2']=rand(5,1)
print(df)

print("--------------------------------------------------")
print("Block 6(removing rows)\n")

print(df.drop('A',0)),print("")
print(df.drop('B'))

print("--------------------------------------------------")
print("Block 7(removing columns)\n")

print(df.drop('Y',1))

print("--------------------------------------------------")
print("Block 8 (inplace or not)\n")
df.drop('Y',1)
print(df)
# NOW PAY ATENTION
df.drop('Y',1,inplace=True)
print(df)


print("--------------------------------------------------")
print("Block 9(slicing data frames)\n")

print(df)
print(df.loc[['A','C'],['X','new-1']])

print("--------------------------------------------------")
print("Block 10(Creating data frame again)\n")

df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

print("--------------------------------------------------")
print("Block 11(Conditional selection part 1)\n")

booldf=df>0
print(booldf)
print("")
print(df[booldf])
print("")
print(df[df>0])
print("")
print(df['W']>0)
print("")
print(df[df['W']>0])
print("")

print("--------------------------------------------------")
print("Block 12(conditional selection part 2)\n")

resultdf=df[df['W']>0]	# it prints the rows for wich the condition is satisfied along column 'W'
print(resultdf)
print("")
print(resultdf['X'])	# it prints the column 'X' of the new data frame 'resultdf'
print("")
# or in one step
print(df[df['W']>0]['X'])			# it does everything above in one step
print(df[df['W']>0][['X','Y']])		# it does everything above but print two columns

print("--------------------------------------------------")
print("Block 13(multiple conditional selection)\n")

print(df[(df['W']>0) & (df['Y']<0.5)])
print("")
print(df[(df['W']>0) | (df['Y']<0.5)])


print("--------------------------------------------------")
print("Block 14(reset the index\n")
print(df)
print("")
print(df.reset_index())



print("--------------------------------------------------")
print("Block 15(adding more columns\n")

states='CA NY WY OR CO'.split()
df['States']=states
print(df)

print("--------------------------------------------------")
print("Block 16(set index)\n")

print(df)
print("")
print(df.set_index('States'))
print("")
print(df)
print("")
#  in place
df.set_index('States',inplace=True)
print("")
print(df)

print("-------------------------------------------------")
print("Block 17(MultiLevels)")

outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)

df=pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)
print("")
# to display rows
print(df.loc['G1'])		# it takes de level G!
print("")
print(df.loc['G1'].loc[1])	# it takes the level G! and then the row '1'
print("")
# to display colums
print(df['A'])
#print(hier_index)


print("-------------------------------------------------")
print("Block 18(creating index names for the levels)")

df.index.names=['Groups','Num']
print(df)		# it will print the data frame with the names on the levels


print("-------------------------------------------------")
print("Block 19(taking information of different groups at the same time)")

print(df)
print("")
print(df.xs(1,level='Num'))






print("-------------------------------------------------")
print("Block 22(MultiLevels)")





print("-------------------------------------------------")
print("Block 23(MultiLevels)")






