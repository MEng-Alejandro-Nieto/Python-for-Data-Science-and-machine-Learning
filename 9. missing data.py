import numpy as np 
import pandas as pd 


d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}

df=pd.DataFrame(d)
print(df)
print("")
print("Block 1 (droping rows and columns) -------------------------------------------")
df2=df.dropna() 	# it will drop all rows  with non value 
print(df2)
print("")
df3=df.dropna(1)	# it will drop all columns with non value
print(df3)
print("")
df4=df.dropna(thresh=2)	# it will drop all rows  with 2 non value or more
print(df4)
print("")
print("Block 2 (filling data)-------------------------------------------")

df5=df.fillna('FILL VALUE')
print(df5)
print("")
# filling a column with the mean value
df6=df['A'].fillna(df['A'].mean())
print(df6)

