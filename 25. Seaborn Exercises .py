import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns



info=sns.load_dataset('titanic')
new_age=info['age'].dropna().apply(lambda x:int(x))
print(info.head(5))

#JOINT PLOT--------------------------------------------------------
#sns.jointplot(x='age',y='fare',data=info)

#DISTRIBUTION PLOT--------------------------------------------------------
#sns.distplot(info['age'].dropna().apply(lambda x:int(x)),kde=False)
#sns.distplot(info['fare'],kde=False,bins=30,color='red')
#sns.distplot(info['fare'])
#sns.distplot(new_age,kde=False,bins=15)

#BOX PLOT--------------------------------------------------------
#sns.boxplot(x='class',y='age',data=info,palette='rainbow')

#VIOLIN PLOT-----------------------------------------------------
#sns.violinplot(x='class',y='age',data=info,palette='rainbow',hue='sex')

#SWARM PLOT------------------------------------------------------
#sns.swarmplot(x='class',y='age',data=info)

#BAR PLOT -------------------------------------------------------
#sns.countplot(info['class'])
#sns.countplot(info['sex'])

#HEAT PLOT-------------------------------------------------------
#pvt_info=info.pivot_table(index='age',columns='embark_town',values='fare')
#sns.heatmap(info.corr())
#plt.title('heat map')

#FACETGRID PLOT--------------------------------------------------
g=sns.FacetGrid(data=info,col='sex')
g.map(plt.hist,'age')
#g.map(sns.distplot,'age')


plt.tight_layout()
plt.show()





































'''
#sns.jointplot(x='fare',y='age',data=info)
#sns.distplot(info['fare'],kde=False,color='red',bins=30)
#sns.boxplot(x='class',y='age',data=info,hue='sex',palette='rainbow')
#sns.swarmplot(x='class',y='age',data=info)
#sns.countplot(info['sex'],data=info)
#sns.heatmap(info.corr())
g=sns.FacetGrid(data=info,col='sex')
g.map(sns.distplot,'age')
plt.tight_layout()
plt.show()


'''