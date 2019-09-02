import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


df1=pd.read_csv('/home/alejandrolive932/Desktop/PYTHON 3/Udemy_Data_Science_and_Machine_Learning/Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df1',index_col=0)
df1['A'].hist(bins=20)
print(df1)


plt.show()



