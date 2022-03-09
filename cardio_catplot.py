# import
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("D:\Github\Visualize-Medical-Data\medical_examination.csv")

# data cleaning
for col in df:
    print(f"{col}:{df[col].unique()}")

# set 1 for not good, 0 for good
df.cholesterol.replace(1, 0, inplace=True)
df.cholesterol.replace([3, 2], 1, inplace=True)
df.gluc.replace(1, 0, inplace=True)
df.gluc.replace([3, 2], 1, inplace=True)
if df.height[0] > 100:
    df.height = df.height / 100

# create overwright column
ow = []
for i in df.index:
    ow.append(1 if (df.weight[i] / (df.height[i] * df.height[i])) > 25 else 0)
df["overweight"] = pd.Series(ow, index=df.index)

# prepare dataframe for catplot
my_columns = ["variable", "cardio", "value", "total"]
df_cat = pd.DataFrame(columns=my_columns)
for i in ["active", "alco", "cholesterol", "gluc", "overweight", "smoke"]:
    for j in df["cardio"].value_counts().index:
        c = df.loc[df["cardio"] == j]
        for v in [0, 1]:
            df_cat = df_cat.append(
                pd.Series([i, j, v, c.loc[c[i] == v].shape[0]], index=my_columns),
                ignore_index=True,
            )

# draw the value counts of the categorical features
fig = sns.catplot(
    x="variable", y="total", hue="value", col="cardio", data=df_cat, kind="bar"
)

# save picture
fig.savefig("cardio-catplot.png")

