import numpy as np

# Create a one-dimensional NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Display the array
print("NumPy Array:", arr)

# Display array properties
print("Dimension:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)

# Perform mathematical operations
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
