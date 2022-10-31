import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

def y_val(x):
  return slope * x + intercept

df = pd.read_csv('height_hair.csv')

# accessing all values from column height & hair_length
x = df.loc[:, 'height']
y = df.loc[:, 'hair_length']

slope, intercept, r, p, std_err = stats.linregress(x, y)

model = []
for i in x:
    model.append(y_val(i))

plt.scatter(x, y, color = 'red')
plt.plot(x, model)
plt.show()

test_set = df.loc[:, 'test_height'] # locating 'test_height' column from 'height_hair.csv'

print("Predictions:\n\ntest heights\tpredicted hair length")
for i in range(5):
    print(f"{test_set[i]}\t\t{round(y_val(test_set[i]), 3)}")