import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sns

rcParams['figure.figsize'] = 8,4
sns.set_style('whitegrid')


x = range(1, 10)
y = [1,2,3,4,0.5,4,3,2,1]

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "gray", "black"]
plt.bar(x, y, color=colors)
plt.title("Simple Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()

z = [1,2,3,4,0.5]
veh_type = ['bicycle', 'motorcycle', 'car', 'van', 'stroller']
plt.pie(z, labels=veh_type)
plt.show()
