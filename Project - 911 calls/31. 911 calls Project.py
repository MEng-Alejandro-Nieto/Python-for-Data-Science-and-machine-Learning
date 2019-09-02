import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

data=pd.read_csv('/home/alejandrolive932/Desktop/PYTHON 3/Udemy_Data_Science_and_Machine_Learning/Refactored_Py_DS_ML_Bootcamp-master/10-Data-Capstone-Projects/911.csv')
print(data.head(5)); print("")
print(data.info()); print("")
# WHAT ARE THE TOP 5 ZIP CODES (zip) FOR 911 CALLS?
print(data['zip'].value_counts().head(5))
print("")

# WHAT ARE THE TOP 5 TOWNSHIPS (twp) FOR 911 CALLS?
print(data['twp'].value_counts().head(5))
print("")

# TAKE A LOOK A T THE "TITLE" COLUMN, HOW MANY UNIQUE TITLE CODES ARE THERE
print(data['title'].nunique())
print("")

# CREATE A NEW COLUMN TO SPECIFY IF THE CALL WAS 'EMS', 'FIRE', 'TRAFFIC' 
print(data['title'])
data['Reason']=data['title'].apply(lambda x:x.split(':')[0] )
print(data['Reason'].value_counts())
print("")

# USE SEABORN TO CREATE A COUNTPLOT OF 911 CALLS BY REASON
#sns.countplot(data['Reason'])
print("")

# WHAT IS THE DATA TYPE OF THE OBJECTS IN THE "TimeStamp" COLUMN
print(data['timeStamp'].apply(lambda x :type(x)))
print("")

# CONVERT THE COLUMN FROM STRINGS TO Datetime OBJECT
data['timeStamp']=pd.to_datetime(data['timeStamp'])
print(data['timeStamp'].apply(lambda x :type(x)))

# AS THE COLUMN TIMESTAMP IS NOW AN OBJECT WE CAN PRINT THE HOUR OUT OF IT 
print(data['timeStamp'].iloc[0].hour)
print("")

# CREATE NEW COLUMN FOR THE Hour, Date of Week, Month
data['Hour']=data['timeStamp'].apply(lambda x:x.hour)
data['Month']=data['timeStamp'].apply(lambda x:x.month)
data['Day of Week']=data['timeStamp'].apply(lambda x:x.dayofweek)
print(data.head(5))

# CREATE A COLUMN THAT DO NOT SHOW THE DAY NUMBER BUT THE NAME
#dmap={'Monday':1,2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
dmap={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
data['Name Day']=data['Day of Week'].map(dmap)
print(data['Name Day'])

# CREATE A COUNT PLOT OF THE DAY OF WEEK COLUMN WITH THE HUE BASED OFF OF THE REASON COLUMN
#sns.countplot(x='Name Day',data=data,hue='Reason')
#plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0)

# DO THE SAME WITH THE MONTH
#sns.countplot(x='Month',data=data,hue='Reason')
#plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0)

# CREATE A LMPLOT() OF A LINEAR FOT ON THE NUMBER OF CALLS PER MONTH.
#y=data.groupby('Month').count().reset_index()
#print(y)
#sns.lmplot(x='Month',y='twp',data=y)

#CREATE A NEW COUMN CALLED 'DATE' THAT CONTAINS THE DATE FROM THE TIMESTAMP
#print(data['timeStamp'].head(5))
data['Date']=data['timeStamp'].apply(lambda x:x.date())
#print(data['Date'])
#data.groupby('Date').count()['lat'].plot()


# CREATE 3 SEPARATE PLOTS WITH EACH PLOT REPRESENTING A REASON FOR 911 CALL
a=data[data['Reason']=='Traffic'].groupby('Date').count().reset_index()['lat']
b=data[data['Reason']=='Fire'].groupby('Date').count().reset_index()['lat']
c=data[data['Reason']=='EMS'].groupby('Date').count().reset_index()['lat']
a.plot()
b.plot()
c.plot()


# REPEAT PROCESS BUT USING FACET GRID
'''
a=data.groupby('Date').count().reset_index()
data['Number Calls']=a['lat']
data.dropna(0,how='any')

print(data['Number Calls'])
print(data['Date'])
g=sns.FacetGrid(data=data,row='Reason')
g.map(plt.plot,'Date','lat')
'''






