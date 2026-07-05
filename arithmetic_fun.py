import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy.stats import pearsonr
from matplotlib import rcParams

np.set_printoptions(precision=2)

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([[10, 20, 30], [40, 50, 60]])

np.random.seed(25)
c = 36 * np.random.randn(6)

d = np.arange(1, 35)

print(a * 10)
print(c + a)
print(c - a)
print(c * a)
print(c / a)

address = "mtcars.csv"

cars = pd.read_csv(address)

cars.columns = [
    "car_names", "mpg", "cyl", "disp", "hp", "drat",
    "wt", "qsec", "vs", "am", "gear", "carb"
]

print(cars.head())

print(cars.sum(numeric_only=True))
print(cars.sum(axis=1, numeric_only=True))
print(cars.median(numeric_only=True))
print(cars.mean(numeric_only=True))
print(cars.std(numeric_only=True))
print(cars.describe())

x = cars[["mpg", "cyl", "qsec", "wt"]]

sns.pairplot(x)
plt.show()

mpg = cars["mpg"]
wt = cars["wt"]

pearsonr_coefficient, p_value = pearsonr(mpg, wt)

print("PearsonR Correlation Coefficient: %0.3f" % pearsonr_coefficient)
print("P-value: %0.3f" % p_value)

corr = x.corr()
print(corr)

corr = x.corr()
print(corr)

sns.heatmap(
    corr,
    xticklabels=corr.columns.values,
    yticklabels=corr.columns.values
)
plt.show()