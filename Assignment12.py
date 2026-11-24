import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Sample customer churn data
data = {
    'Age': [24, 27, 22, 32, 29, 25, 100],
    'Salary': [50000, 60000, 52000, 58000, 62000, 55000, 600000],
    'Tenure': [1, 2, 3, 5, 4, 2, 10],
    'Churn': ['Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

print("Original Customer Dataset:")
print(df)

# 1. Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

print("\nMean Age:", df['Age'].mean())
print("Median Age:", df['Age'].median())
print("Mode Age:", df['Age'].mode()[0])
print("Standard Deviation:", df['Age'].std())
print("Variance:", df['Age'].var())
print("Minimum Age:", df['Age'].min())
print("Maximum Age:", df['Age'].max())
print("Quantiles:")
print(df['Age'].quantile([0.25, 0.5, 0.75]))

# 2. Visualization and Plotting

# Histogram
plt.hist(df['Age'], bins=5, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Box Plot
sns.boxplot(y=df['Age'])
plt.title('Box Plot of Age')
plt.show()

# Scatter Plot
plt.scatter(df['Age'], df['Salary'])
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# Correlation Matrix
corr_matrix = df[['Age', 'Salary', 'Tenure']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 3. Handling Missing Data

# Introduce missing values for demonstration
df.loc[2, 'Age'] = None
df.loc[3, 'Salary'] = None

print("\nMissing Values:")
print(df.isnull())

# Remove rows with missing values
df_dropped = df.dropna()
print("\nAfter Removing Missing Values:")
print(df_dropped)

# Fill missing values with column means
df_filled = df.fillna(df.mean(numeric_only=True))
print("\nAfter Filling Missing Values:")
print(df_filled)

# 4. Handling Outliers

# Detect outliers using z-scores
df['Age_zscore'] = zscore(df['Age'])
df['Salary_zscore'] = zscore(df['Salary'])

print("\nDataset with Z-scores:")
print(df)

# Remove outliers
df_no_outliers = df[
    (df['Age_zscore'].abs() <= 3) &
    (df['Salary_zscore'].abs() <= 3)
]

print("\nAfter Removing Outliers:")
print(df_no_outliers)

# Cap outliers
def cap_values(series):
    upper_limit = series.mean() + 3 * series.std()
    lower_limit = series.mean() - 3 * series.std()
    return series.clip(lower=lower_limit, upper=upper_limit)

df['Age_capped'] = cap_values(df['Age'])
df['Salary_capped'] = cap_values(df['Salary'])

print("\nAfter Capping Outliers:")
print(df[['Age', 'Age_capped', 'Salary', 'Salary_capped']])

print("\nEDA Completed Successfully!")
