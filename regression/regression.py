# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 20:29:57 2025

@author: diya
# """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

# Simulated data
np.random.seed(42)
x = np.random.uniform(5, 30, 25)  # delivery volume in cases
y = 3.5 + 2 * x + np.random.normal(0, 2, size=25)  # delivery time

# Put in a DataFrame
df = pd.DataFrame({'DeliveryVolume': x, 'DeliveryTime': y})

# Scatterplot
plt.scatter(x='DeliveryVolume', y='DeliveryTime', data=df)
plt.title("Delivery Time vs Volume")
plt.show()

import statsmodels.api as sm

X = sm.add_constant(df['DeliveryVolume'])  # Adds intercept term
model = sm.OLS(df['DeliveryTime'], X).fit()

# Summary of results
print(model.summary())

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)

print(speed)

import scipy
print(scipy.__version__)

