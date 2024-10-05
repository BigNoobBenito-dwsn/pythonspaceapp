import pandas as pd
import numpy as np
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia
import astropy.units as u
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
angle = 0.2
finaldf = None
increment = 60
ra = 10
dec =10
scanscope = 20
a = True
min = 0
max = 360
while (angle <= max and a):
        coord = SkyCoord(ra=angle, dec=0, unit=(u.degree, u.degree), frame='icrs')
        width = u.Quantity(0.1, u.deg)
        height = u.Quantity(0.1, u.deg)
        r = Gaia.query_object_async(coordinate=coord, width=width, height=height)
        if (finaldf is None):
            finaldf = df.copy()
        else:
            finaldf = pd.concat([finaldf,df])
        angle+=0.05
        print(angle)
print(finaldf)
finaldf.to_csv(max+'final.csv')
