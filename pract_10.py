
import numpy as np

# Create a one-dimensional array
arr = np.arange(1, 11)

print("Original Array:", arr)

# Slicing operations
print("First 5 Elements:", arr[:5])
print("Last 5 Elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])
print("Every 2nd Element:", arr[::2])

# Statistical operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting
arr = arr + 5
print("After Adding 5:", arr)

arr = arr * 2
print("After Multiplying by 2:", arr)
