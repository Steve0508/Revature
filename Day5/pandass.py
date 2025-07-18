import pandas as pd

# Series
s = pd.Series([10, 20, 30])
print(s)

# DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 20, 21]
}
df = pd.DataFrame(data)
print(df)

# ✅ Read CSV correctly
df = pd.read_csv('data.csv')

# ✅ Write CSV
df.to_csv('output.csv', index=False)

# ✅ Read Excel correctly
df = pd.read_excel('data.xlsx', engine='openpyxl')

# ✅ Write Excel
df.to_excel('output.xlsx', index=False)

# Explore Data
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)

# Data Selection
df['Name']
df[['Name','Age']]  #Multiple columns
df.iloc[0]  #first row( by index)
df.loc[0,'Name'] #specific value


#Filtering Rows]

df[df['Age']> 25]    #Age>25
df[(df['Age']>25) & (df['Age']<35)] #derived Column



#adding /Modifying columns
df['Salary']=[50000,60000,70000]  #new column
df['Age in 5 Years']=df['Age']+5   #Derived column


#sorting and Grouping


df.sort_values(by='Age',ascending=False)

df.groupby('Name')['Age'].mean()

#Handling missing data

df.isnull() #check for NaN
df.dropna() #Drop rows with Nan

df.fillna(0) #Replace NaN with 0


