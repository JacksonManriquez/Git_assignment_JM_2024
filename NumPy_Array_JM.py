import numpy as np
###Step 1
a = np.random.randint(0, 255, size=(5, 5), dtype=int)

###Step 2
print("Entire array")
print(a)

###Step 3
print("Data in second row, third column")
print(a[1, 2])

###Step 4
print("Sum of entire array")
print(a.sum())

###Step 5
print("Mean of each row")
print(np.mean(a, axis=0))

###Step 6
print("The highest value in every column")
print(np.max(a, axis=0))
