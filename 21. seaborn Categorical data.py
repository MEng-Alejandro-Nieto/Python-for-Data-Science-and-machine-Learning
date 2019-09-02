import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
tips= sns.load_dataset('tips')

print(tips.head(5))

#sns.distplot(tips['total_bill'])
#sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.mean)
#sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
#sns.countplot(x='sex',data=tips)
#sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')
#sns.violinplot(x='day',y='total_bill',data=tips)
#sns.violinplot(x='day',y='total_bill',data=tips,hue='sex')
#sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)
#sns.stripplot(x='day',y='total_bill',data=tips)
#sns.stripplot(x='day',y='total_bill',data=tips,hue='sex')
#sns.swarmplot(x='day',y='total_bill',data=tips,hue='sex') # do  not use it when dealing with large set of data
#sns.factorplot(x='day',y='total_bill',data=tips,hue='sex',kind='bar')
sns.factorplot(x='day',y='total_bill',data=tips,hue='sex',kind='violin')
plt.tight_layout()
plt.show()





