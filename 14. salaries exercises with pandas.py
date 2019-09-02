
import numpy as np 
import pandas as pd 


table=pd.read_csv('/home/alejandrolive932/Desktop/Udemy_Data_Science_and_Machine_Learning/Refactored_Py_DS_ML_Bootcamp-master/04_Pandas_Exercises/Salaries.csv')

print(table)

print("------------------------------------------------\n")

print(table.head(5))

print("------------------------------------------------\n")

print(table.info())

print("------------------------------------------------\n")

print(table['BasePay'].mean())

print("------------------------------------------------\n")

print(table['OvertimePay'].max())

print("------------------------------------------------\n")

print(table[table['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])

print("------------------------------------------------\n")

print(table[table['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])

print("------------------------------------------------\n")

print(table[table['TotalPayBenefits'].max()==table['TotalPayBenefits']]['EmployeeName'])

print("------------------------------------------------\n")

print(table[table['TotalPayBenefits'].min()==table['TotalPayBenefits']]['EmployeeName'])

print("------------------------------------------------")

print(table.groupby('Year').mean()['BasePay'])

print("------------------------------------------------")

print(table['JobTitle'].nunique())


print("------------------------------------------------")

print(table['JobTitle'].value_counts().head(5))

print("------------------------------------------------")

print(sum(table[table['Year']==2013]['JobTitle'].value_counts()==1))

print("------------------------------------------------")

print(sum(table['JobTitle'].apply(lambda x:'chief'in x.lower().split())))

'''
def chief(word):
	if 'chief' in word.lower().split():
		return True
	else:
		return False

print(sum(table[table['JobTitle'].apply(lambda word:chief(word))]['JobTitle'].value_counts()))
print(sum(table['JobTitle'].apply(lambda word:chief(word))))
'''
print("------------------------------------------------")


'''
table=pd.read_csv('Salaries.csv')
print(table)
print("----------------------------------------------------\n")
print("print the head of the table")
print(table.head())
print("----------------------------------------------------\n")
print("print the first 4 rows of the table")
print(table.head(4))
print("----------------------------------------------------\n")
print("print how many rows and columns there are in 'table'")
print(table.info())
print("----------------------------------------------------\n")
print("print what is the average 'BasePay'")
print(table['BasePay'].mean())
print("----------------------------------------------------\n")
print("print the highest amount of 'Overtimepay' in 'Table'")
print(table['OvertimePay'].max())
print("----------------------------------------------------\n")
print("what is the job title of JOSEPH DRISCOLL? ")
# 1 step 
print(table['EmployeeName']=='JOSEPH DRISCOLL')
# 2 step
print(table[table['EmployeeName']=='JOSEPH DRISCOLL'])
# 3 step
print(table[table['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])
print("----------------------------------------------------\n")
print("what is total salary of JOSEPH DRISCOLL? ")
# 1 step
print(table['EmployeeName']=='JOSEPH DRISCOLL')
# 2 step
print(table[table['EmployeeName']=='JOSEPH DRISCOLL'])
print(type(table[table['EmployeeName']=='JOSEPH DRISCOLL']))
# 3 step
print(table[table['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])
print("----------------------------------------------------\n")
print("print the name of the person with highest paid ")
#1 step
print(table['TotalPayBenefits'].max())
# 2 step
print(table['TotalPayBenefits']==table['TotalPayBenefits'].max())
# 3 step
print(table[table['TotalPayBenefits']==table['TotalPayBenefits'].max()])
# 4 step
print(table[table['TotalPayBenefits']==table['TotalPayBenefits'].max()]['EmployeeName'])
print("----------------------------------------------------\n")
print("print the name of the person with lowest paid ")
#1 step
print(table['TotalPayBenefits'].min())
# 2 step
print(table['TotalPayBenefits']==table['TotalPayBenefits'].min())
# 3 step
print(table[table['TotalPayBenefits']==table['TotalPayBenefits'].min()])
# 4 step
print(table[table['TotalPayBenefits']==table['TotalPayBenefits'].min()]['EmployeeName'])
print("----------------------------------------------------\n")
print("what was the average BasePay of all empolyees per year (2011-2014)?")
print(table.groupby('Year').mean()['BasePay'])
print("----------------------------------------------------\n")
print("How many unique title are there")
print(table['JobTitle'].nunique())
# or
print(len(table['JobTitle'].unique()))
print("----------------------------------------------------\n")
print("What are the top 5 most common jobs")
# 1 step
print(f"{table['JobTitle']}\n")
# 2 step
print(f"{table['JobTitle'].value_counts()}\n")
# 3 step
print(f"{table['JobTitle'].value_counts().head(5)}\n")
print("----------------------------------------------------\n")
print("how many jobs titles were represented by only one person in 2013 ?")
print(table[table['Year']==2013]['JobTitle'].value_counts()==1)
print(sum(table[table['Year']==2013]['JobTitle'].value_counts()==1))
print("----------------------------------------------------\n")
print("How many people have the word chief in their job title?")
print(table['JobTitle'])

def chief(table):
	if 'chief' in table.lower().split():
		return True
	else:
		return False

print(sum(table['JobTitle'].apply(lambda x:chief(x))))

'''























