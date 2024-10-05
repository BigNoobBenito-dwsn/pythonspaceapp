import math

import astropy.units as u
import pandas as pd

from pandas import DataFrame, Series
import numpy as np
Gaia.ROW_LIMIT = -1
def remove_uselesscoloumn(data):
    return data.drop(data.columns.difference(['ra', 'dec',"parallax", ""]), axis=1)
def removenanvalue(data):
    return data.dropna()
def findcoordonate(data):
    data["X"] = (1000 / data['parallax']) * np.sin(data['ra'])np.cos(data['dec'])
    data["Y"] = (1000 / data['parallax']) np.sin(data['ra'])np.sin(data['dec'])
    data["Z"]=(1000 / data['parallax'])np.cos(data['ra'])
    return data
def removeradecparallax(data):
    return data.drop(['ra', 'dec', "parallax"], axis=1)
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
        data = r.to_pandas()
        data = removeradecparallax(findcoordonate(removenanvalue(remove_uselesscoloumn(data))))
        if (finaldf is None):
            finaldf = data.copy()
        else:
            finaldf = pd.concat([finaldf,data])
        angle+=0.05
        print(angle)
print(finaldf)
finaldf.to_csv(max+'final.csv')
