import numpy as np 
import pandas as pd 

df1=pd.DataFrame({'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']},index=[0,1,2,3])
df2=pd.DataFrame({'A':['A4','A5','A6','A7'],'B':['B4','B5','B6','B7'],'C':['C4','C5','C6','C7'],'D':['D4','D5','D6','D7']},index=[4,5,6,7])
df3=pd.DataFrame({'A':['A8','A9','A10','A11'],'B':['B8','B9','B10','B11'],'C':['C8','C9','C10','C11'],'D':['D8','D9','D10','D11']},index=[8,9,10,11])

print(f"{df1}\n")
print(f"{df2}\n")
print(f"{df3}\n")

print("1. Concatenation ---------------------------------------")
print(f"{pd.concat([df1,df2,df3])}\n")
print(f"{pd.concat([df1,df2,df3],axis=1)}\n")

print("2. another example--------------------------------------")
left=pd.DataFrame({'key':['K0','K1','K2','K3'],'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3'],})
right=pd.DataFrame({'key':['K0','K1','K2','K3'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3'],})

print(f"{left}\n")
print(f"{right}\n")

print(f"{pd.concat([left,right],axis=0,sort=True)}\n")
print(f"{pd.concat([left,right],axis=1,sort=True)}\n")

print("3. Merging----------------------------------------------")

print(f"this is data frame 'left':\n{left}\n")
print(f"this is data frame 'right':\n{right}\n")
# we will merge now these last to data frames in the 'key' column
print(f"this is 'left' and 'right' merged:\n{pd.merge(left,right,how='inner',on='key')}\n")

print("4. Joining----------------------------------------------")

left=pd.DataFrame({'A':['A0','A1','A2'],'B':['B0','B1','B2']},index=['k0','k1','k2'])
right=pd.DataFrame({'C':['C0','C1','C2'],'D':['D0','D1','D2']},index=['k0','k2','k3'])

print(f"this is data frame 'left':\n{left}\n")
print(f"this is data frame 'right':\n{right}\n")

print(f"this is left joined to right:\n{left.join(right)}\n")
print(f"this is left joined to right:\n{left.join(right,how='outer')}\n")
print(f"this is left joined to right:\n{left.join(right,how='inner')}\n")







