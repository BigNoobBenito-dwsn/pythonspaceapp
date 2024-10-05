import pandas as pd
import numpy as np
df = pd.read_csv('PS_2024.10.05_11.27.16.csv')
columns_to_keep = ['pl_name', 'pl_refname', 'ra', 'dec', 'sy_dist']
df = df[columns_to_keep]
df = df.drop_duplicates()
df = df.dropna()
print(df.head())
df['parallax'] = (1/ df['sy_dist'])  * 1000
print(df.head())
df["X"] = (1000 / df['parallax']) * np.sin(df['ra'])* np.cos(df['dec'])
df["Y"] = (1000 / df['parallax'])* np.sin(df['ra']) * np.sin(df['dec'])
df["Z"] = (1000 / df['parallax']) * np.cos(df['ra'])
print(df.head())
