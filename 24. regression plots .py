import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

tips=sns.load_dataset('tips')
print(tips.head())

#sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')
#sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'])
#sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')
#sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='time')
#sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='time',hue='sex',aspect=0.8,size=3)
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='time',hue='sex',aspect=0.8,size=3)

plt.tight_layout()
plt.show()













