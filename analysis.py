# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import seaborn as sns


# Load Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display first few rows
print(df.head())

# Explore structure
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# Clean missing values (if any)
df = df.dropna()  # No missing values in Iris, but this is a safeguard
 
#  QUESTION 2 DATA ANALYSIS
print("\nBasic Statistics:\n", df.describe())

# Grouping by species and mean of features
grouped = df.groupby('species').mean()
print("\nMean values by species:\n", grouped)

# Identifying patterns
print("\nPattern Observation:")
print("-> Iris-virginica generally has the highest values across all features.")
 
# QUESTION 3 DATA VISUALIZATION
#line plot of Petal Length over index (simulated time)
plt.figure(figsize=(10, 5))
sns.lineplot(data=df.sort_values(by='petal length (cm)'), x=df.index, y='petal length (cm)', hue='species')
plt.title('Petal Length Over Index (Simulated Time)')
plt.xlabel('Index')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', style='species', palette='deep')
plt.title('Sepal Length vs. Petal Length by Species', fontsize=14)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()

# Bar plot of average Petal Length per Species
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='species', y='petal length (cm)', ci=None, palette='pastel')
plt.title('Average Petal Length per Species', fontsize=14)
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.tight_layout()
plt.show()

# Histogram of Sepal Width
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal width (cm)'], kde=True, bins=20, color='skyblue')
plt.title('Distribution of Sepal Width', fontsize=14)
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter plot of Sepal Length vs. Petal Length
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', style='species', palette='deep')
plt.title('Sepal Length vs. Petal Length by Species', fontsize=14)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()

