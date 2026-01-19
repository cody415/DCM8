import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [35000, 48000, 39000, 52000, 41000]
}

df = pd.DataFrame(data)

# 1. Bar Chart – Salary by Employee
plt.bar(df['Name'], df['Salary'])
plt.title('Salary by Employee')
plt.xlabel('Employee')
plt.ylabel('Salary')
plt.show()

# 2. Histogram – Age Distribution
plt.hist(df['Age'], bins=5, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 3. Pie Chart – Department Proportion
dept_counts = df['Department'].value_counts()
plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%')
plt.title('Department Distribution')
plt.show()

# 4. Line Chart – Salary Trend by Age
plt.plot(df['Age'], df['Salary'], marker='o')
plt.title('Salary Trend by Age')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# 5. Scatter Plot – Age vs Salary
plt.scatter(df['Age'], df['Salary'], color='red')
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()
