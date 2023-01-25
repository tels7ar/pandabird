"""
Test some pandas stuff.
"""

import pandas as pd


def clean(mystring: str) -> str:
    mystring = mystring[1:]
    return mystring


# df1_data = {"ID": ["1", "1", "3", "4", "2", "3"], "Date": ["1/1/20", "1/5/20", "5/2/21", "7/4/19", "12/2/19", ""]}
# df2_data = {"ID": ["1", "2", "3", "4", "5"], "Sex": ["M", "M", "F", "F", "M"], "Chord": ["", 3.5, 1, 4.32, 2.2]}
# df1 = pd.DataFrame(df1_data)
# df2 = pd.DataFrame(df2_data)

df1 = pd.read_csv("/Users/phollenb/git/pandabird/merge/SBFreqsProps.csv")
df2 = pd.read_csv("/Users/phollenb/git/pandabird/merge/Biometrics.csv")

# For some reason the IDs start with 'X' in df1 data.
# Use clean function to remove first letter from each
df1["ID"] = df1["ID"].apply(clean)

print("df1:")
print(df1)
print()

print("df2:")
print(df2)
print()

df3 = pd.merge(df1, df2, on="ID", how="left")

# sex is same in both dataframes so just drop the sex we got from df2
# and rename Sex_x to Sex.
df3 = df3.drop("Sex_y", axis=1)
df3.rename(columns={"Sex_x": "Sex"}, inplace=True)

# don't truncate the column list when displaying.
pd.set_option("expand_frame_repr", False)

print("df1 merged with df2:")
print(df3)
