"""
Test some pandas stuff.
"""

import pandas as pd

df1_data = {"ID": ["1", "1", "3", "4", "2", "3"], "Date": ["1/1/20", "1/5/20", "5/2/21", "7/4/19", "12/2/19", ""]}
df2_data = {"ID": ["1", "2", "3", "4", "5"], "Sex": ["M", "M", "F", "F", "M"], "Chord": ["", 3.5, 1, 4.32, 2.2]}

df1 = pd.DataFrame(df1_data)
df2 = pd.DataFrame(df2_data)

print("df1:")
print(df1)
print()

print("df2:")
print(df2)
print()

df3 = pd.merge(df1, df2, on="ID", how="left")

print("df1 merged with df2:")
print(df3)
