import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [35000, 48000, 39000, 52000, 41000]
}

df = pd.DataFrame(data)
print(df)

print(df.head(3))
print(df.dtypes)
print(df.describe())

print(df[['Name', 'Salary']])
print(df[df['Age'] > 25])
print(df[df['Department'] == 'IT'])

df['Bonus'] = df['Salary'] * 0.10
df['Salary'] = df['Salary'] * 1.05
print(df)

print(df.groupby('Department')['Salary'].mean())
print(df['Department'].value_counts())

print(df.sort_values(by='Age'))
print(df.sort_values(by='Salary', ascending=False))

df.loc[2, 'Salary'] = None
print(df)
print(df.isnull().sum())
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)

df['AgeGroup'] = pd.cut(df['Age'], bins=[20, 25, 30, 35], labels=['20-25','26-30','31-35'])
pivot = pd.pivot_table(df, values='Salary', index='Department', columns='AgeGroup', aggfunc='mean')
print(pivot)
