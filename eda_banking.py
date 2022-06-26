# -*- coding: utf-8 -*-
"""EDA_Banking.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yuN7I05fw6dzyYMZ1lS-MaujMUJNIpTz
"""

!wget https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank-additional.zip

!unzip -o -q bank-additional.zip

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline
plt.rcParams["figure.figsize"] = (8, 6)

import warnings
warnings.filterwarnings('ignore')

pd.set_option("precision", 2)
pd.options.display.float_format = '{:.2f}'.format

df = pd.read_csv('bank-additional/bank-additional-full.csv', sep = ';')
df.head(5)

df.shape

df.columns

print(df.info())

df.describe()

df.describe(include = ["object"])

df["y"].value_counts()

df["marital"].value_counts()

df["marital"].value_counts(normalize = True)

df.sort_values(by = "duration", ascending = False).head()

df.sort_values(by = ["age", "duration"], ascending = [True, False]).head()

df.apply(np.max)

d = {"no": 0, "yes": 1}
df["y"] = df["y"].map(d)
df.head()

print("Share of attracted clients =", '{:.1%}'.format(df["y"].mean()))

df[df["y"] == 1].mean()

acd = round(df[df["y"] == 1]["duration"].mean(), 2)
acd_in_min = acd // 60
print("Average call duration for attracted clients =", acd_in_min, "min", int(acd) % 60, "sec")

print("Average age of attracted clients =", int(df[(df["y"] == 1) & (df["marital"] == "single")]["age"].mean()), "years")

df[-1:]

pd.crosstab(df["y"], df["marital"])

pd.crosstab(df["y"],
            df["marital"],
            normalize = 'index')

df.pivot_table(
    ["age", "duration"],
    ["job"],
    aggfunc = "mean",
).head(10)

df["age"].hist()

df.hist(color = "k",
        bins = 30,
        figsize = (15, 10))
plt.show()

df.boxplot(column = "age",
           by = "marital")
plt.show()

df.boxplot(column = "age",
           by = ["marital", "housing"],
           figsize = (20, 20))

df.sort_values(by = "campaign", ascending = False).head(10)

df.pivot_table(
    ["age", "campaign"],
    ["education"],
    aggfunc = ["mean", "count"],
)

df.boxplot(column = "age",
  by = "education",
  figsize = (15, 15))
