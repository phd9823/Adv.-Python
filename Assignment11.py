import pandas as pd
import numpy as np

# Generate 10 random numbers
numbers = np.random.randint(1, 100, 10)

# Create a Pandas Series
series = pd.Series(numbers)

# Display the Series
print("Pandas Series:")
print(series)

# Display basic information
print("\nMean:", series.mean())
print("Maximum:", series.max())
print("Minimum:", series.min())
print("Sum:", series.sum())
