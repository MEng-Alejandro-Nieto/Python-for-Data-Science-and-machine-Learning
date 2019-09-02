import numpy as np 
import pandas as pd 

data={'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],'Name':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],'Sales':[200,120,340,124,243,350]}

print("Block 1-------------------------------------------")

df=pd.DataFrame(data)
print(df)

print("Block 2  (Group by company and operations) -------------------------------------------")
byComp=df.groupby('Company')

print(f"{byComp.mean()}\n")
print(f"{byComp.sum()}\n")
print(f"{byComp.std()}\n")
print(f"{byComp.sum().loc['FB']}\n")
print(f"{byComp.count()}\n")
print(f"{byComp.max()}\n")
print(f"{byComp.min()}\n")


print("Block 3 (describe function)-------------------------------------------")

print(f"{df.groupby('Company').describe()}\n")
print(f"{df.groupby('Company').describe().transpose()}\n")
print(f"{df.groupby('Company').describe().transpose()['FB']}\n")

