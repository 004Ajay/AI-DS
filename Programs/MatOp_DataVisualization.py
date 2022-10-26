import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

mat = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
mat2 = np.array([[5, 6],
                   [-1, 2]])

print("Martrix 1:\n", mat)
print("\nMatrix Addition:\n", mat + mat, "\n\nMatrix Subtraction:\n", mat - mat)
print("\nMatrix Multiplication:\n", mat * mat, "\n\nMatrix Division:\n", mat / mat)
print("\nMatrix Exponentiation:\n", mat ** 2, "\n\nMatrix Transpose:\n", mat.T)

# data
x = np.arange(0, 10)
y = np.arange(11, 21)


# plotting using matplotlib
plt.scatter(x, y, c='g')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Plotting using Matplotlib')
plt.show()

# plotting using seaborn
grf = sns.stripplot(x)
grf.set(xlabel='X axis', ylabel='Y axis', title='Plotting using Seaborn')
plt.show()

# ---------------------------------------------------------------------------------- #

