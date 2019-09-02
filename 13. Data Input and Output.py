'''

CSV files
Excel
HTML
SQL


to open HTML and SQL files install :
pip install sqlalchemy
pip install lxml
pip install html5lib
pip install beautifulsoup4
'''

import pandas as pd 
print("READING AND WRITING A CSV FILE\n")
# READING A CSV FILE
table=pd.read_csv('/home/alejandrolive932/Desktop/Udemy_Data_Science_and_Machine_Learning/Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/example')
print(table)

# WRITING TO A SCV FILE
df=pd.read_csv('/home/alejandrolive932/Desktop/Udemy_Data_Science_and_Machine_Learning/Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/example')

df.to_csv('My_output')	# save df as 'My_output' with unnamed column
print("")
print(pd.read_csv('My_output'))		# it reads the file just created

df.to_csv('My_output',index=False)	# save df as 'My_output'
print("")
print(pd.read_csv('My_output'))
#--------------------------------------------------------------
print("READING AND WRITING AN EXCEL FILE\n")
# READING A EXCEL FILE
df=pd.read_excel('/home/alejandrolive932/Desktop/Udemy_Data_Science_and_Machine_Learning/Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/Excel_Sample.xlsx',sheet_name='Sheet2')
print(df)

# WRITING TO AN EXCEL FILE
df.to_excel('Excel_sample2.xlsx',sheet_name='NewSheet')








