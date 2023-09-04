import pandas as pd
import numpy as np

df = pd.read_csv('chipotle.tsv', sep = '\t')


#observing the dataframe
print(df.head(10))

#checking the datatypes of the colums
print(df.info())


#removing the dollar sign in the item price 
df['item_price'] = df['item_price'].str.replace('$', ' ')

#changing the datatype to float
df['item_price'] = df['item_price'].astype('float64')

print(df['item_price'].head(4))

#confirming new change 
for colum, datatype in zip(df.columns, df.dtypes):
    print(f"{colum}: {datatype}")


#checking null values

dataset_null = df.isnull().sum()
print(dataset_null)

#we can see that choice description is the only null values in this dataset. Checking the percentage of  null values in each column. if it's up to 70% we can drop the column

percentage_missing = df.isnull().mean()*100

print(percentage_missing)


#understanding the null values in the choice_description column, we first check the unique entries in that column to understand what it’s about. Let’s check the unique item for this description to have more idea.

distinct_entries = df.loc[df['choice_description'].isnull(), 'item_name'].unique()
print(distinct_entries)

#Now we check how many unique item_name have null choice_description

count_distinct_entries= df[df['choice_description'].isnull()]['item_name'].nunique()
print("Number of unique item_name with null description:", count_distinct_entries)

#Since, these missing values are for the choice of customer: For the moment, let’s assume that those customers didn’t mention their choices. So we can replace these missing values by ‘Regular’ or “no preferred choice”. For the sake of continuity, we choose Regular. Now, let’s replace the null values by ‘Regular Order’. 
df['choice_description'] = df['choice_description'].fillna('Regular Order')


#checking to see if there's anymore null values
print(df.isnull().sum())


#checking duplicate rows 
count_duplicates = df[df.duplicated()].shape[0]
print("Number of duplicate rows:", count_duplicates)

#view of duplicate entries
duplicates = df[df.duplicated(keep = False)]

duplicates_sorted = duplicates.sort_values(by=['order_id'])

print(duplicates_sorted.to_string(index = False))

#delete duplicate entries
df.drop_duplicates(inplace = True)


#checking to see if duplicates are removed
print("Number of duplicate rows: ", df[df.duplicated()].shape[0])


#removing extra space
for col in df.columns:
    if df[col].dtypes == 'object':
        df[col] = df[col].str.strip()
        
#save the cleaned dataset
df.to_csv('cleaned_dataset.csv', index = False)