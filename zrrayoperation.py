import numpy as np

# 1. Creating Arrays
arr1 = np.arange(1, 11)              # 1D array from 1 to 10
arr2 = np.zeros((3, 3))              # 3x3 zeros
arr3 = np.ones((3, 3))               # 3x3 ones
arr4 = np.random.rand(5)             # 5 random numbers between 0 and 1

# 2. Basic Operations
print(arr1.sum())                    # Sum
print(arr1.mean())                   # Mean
print(arr1.std())                    # Standard deviation
print(arr1 * 2)                      # Multiply by 2
print(arr2 + arr3)                   # Add arrays

# 3. Indexing and Slicing
print(arr1[:5])                      # First 5 elements
print(arr1[-3:])                     # Last 3 elements
print(arr3[1, :])                    # Second row of arr3

# 4. Reshaping
print(arr1.reshape(2, 5))            # Reshape to 2x5
print(arr3.flatten())                # Flatten to 1D

# 5. Mathematical Operations
print(np.square(arr1))               # Square each element
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a, b))                  # Dot product
print(np.maximum(a, b))              # Element-wise maximum

# 6. Logical Operations
print(arr1 > 5)                      # Elements greater than 5
print(np.sum(arr1 % 2 == 0))         # Count even numbers

# 7. Advanced Challenge
arr5 = np.random.randint(1, 21, (4, 4))  # 4x4 random integers between 1 and 20
print(arr5.max(axis=1))                  # Max in each row
print(np.sort(arr5, axis=0))             # Sort by columns
