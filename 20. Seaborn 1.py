import seaborn as sns
import pandas as pandas
import numpy as np
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
print(tips.columns)
print(tips)
print(len(tips['total_bill']))

#sns.distplot(tips['total_bill'],kde=False,bins=10)
#sns.jointplot(x='total_bill',y='tip',data=tips)
#sns.pairplot(tips,hue='sex')
sns.rugplot(tips['total_bill'])
plt.tight_layout()
plt.show()












