import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("Employee_Attrition_Dataset_With_Errors.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Age with Mean
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Replace Blank Department with Unknown
df['Department'].replace('', 'Unknown', inplace=True)

# Standardize Gender Column
df['Gender'] = df['Gender'].replace({
    'M': 'Male',
    'F': 'Female'
})

# Standardize Marital Status
df['MaritalStatus'] = df['MaritalStatus'].replace({
    'married': 'Married'
})

# Handle Negative Salary
df.loc[df['MonthlySalary'] < 0, 'MonthlySalary'] = np.nan
df['MonthlySalary'].fillna(df['MonthlySalary'].mean(), inplace=True)

# Handle Negative YearsAtCompany
df.loc[df['YearsAtCompany'] < 0, 'YearsAtCompany'] = 0

# Fix Invalid Job Satisfaction Values
df.loc[df['JobSatisfaction'] > 5, 'JobSatisfaction'] = 5

# Remove Duplicate Records
duplicates = df.duplicated().sum()
print("\nNumber of Duplicates:", duplicates)

df = df.drop_duplicates()

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Attrition Distribution
print("\nAttrition Count:")
print(df['Attrition'].value_counts())

# Save Cleaned Dataset
df.to_csv("Cleaned_Employee_Attrition_Dataset.csv", index=False)

print("\nData Cleaning Completed Successfully!")