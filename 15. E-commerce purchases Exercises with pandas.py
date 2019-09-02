import pandas as pd 


table=pd.read_csv('/home/alejandrolive932/Desktop/Udemy_Data_Science_and_Machine_Learning/Refactored_Py_DS_ML_Bootcamp-master/04_Pandas_Exercises/Ecommerce Purchases')
print(table.info())
# 1. Check the head of the DataFrame
print(table.head())


# 2. How many columns and rows there are

print(f"the number of rows are : {table.index.nunique()}")
print(f"the number of columns are : {table.columns.nunique()}")


# 3. What is the average Purchase Price?

print(f"the average purchase price is : {table['Purchase Price'].mean()}")


# 4. What is the highest  and lowest prices?

print(f"the highest price is: {table['Purchase Price'].max()}")
print(f"the lowest price is: {table['Purchase Price'].min()}")


# 5. How many people have English 'en' as their language of choice on the website

print(f"the number of people that have english as their language are: {sum(table['Language'].apply(lambda x:'en' in x.lower().split()))}")

# 6. How many people have the job title of 'Lawyer'
print(f"the number of people with 'Lawyer' as a title are: {sum(table['Job'].apply(lambda x:x=='Lawyer'))}")
print(f"{sum(table['Job']=='Lawyer')}")


# 7. How many people made the purchase during AM and PM
print(f"{table['AM or PM'].value_counts()}")

# 8. What are the five most common jobs Titles?

print(f"the five most common jobs are:\n{table['Job'].value_counts().head(5)}")

# 9. Someone made a purchase that came from Lot:'90 WT', what 
# was the purchase Price for this transaction

print(f"the price for this transaction was: {table[table['Lot']=='90 WT']['Purchase Price']}\n")

# 10.What is the email of the person with the following Credit Card Number

print(table[(table['Credit Card']==4926535242672853)]['Email'])


# 11. How many people have american express as their credit 
# card provider and a purchase above 95 dollars

print(len(table[(table['CC Provider']=='American Express') & (table['Purchase Price']>95)]))


# 12 How may people have credit card that expires in 2025

print(f"{sum(table['CC Exp Date'].apply(lambda x:'/25' in x))}\n")


# 13 What are the top 5 most popular email providers/host (e.g. gmail.com. yahoo.com etc)


print(table['Email'].apply(lambda x:x.split('@')[1]).value_counts().head(5))