import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [35000, 48000, 39000, 52000, 41000]
}

df = pd.DataFrame(data)

sns.barplot(x='Name', y='Salary', data=df)
plt.title('Salary by Employee')
plt.show()

sns.histplot(df['Age'], bins=5, kde=True)
plt.title('Age Distribution')
plt.show()

sns.countplot(x='Department', data=df)
plt.title('Department Count')
plt.show()

sns.lineplot(x='Age', y='Salary', data=df, marker='o')
plt.title('Salary Trend by Age')
plt.show()

sns.scatterplot(x='Age', y='Salary', hue='Department', data=df, s=100)
plt.title('Age vs Salary by Department')
plt.show()

sns.boxplot(x='Department', y='Salary', data=df)
plt.title('Salary Distribution by Department')
plt.show()
