import pandas as pd

df = pd.read_csv('book.csv', header = 0)
col = df['values']

print(f"Before sorting:\n{df.to_string(index=False)}\n\nAfter sorting: {sorted(col)}")