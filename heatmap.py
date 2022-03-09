# import data
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("D:\Github\Visualize-Medical-Data\medical_examination.csv")

# handle data
df["overweight"] = (df["weight"] / (df["height"] / 100) ** 2).apply(
    lambda x: 1 if x > 25 else 0
)
df["cholesterol"] = df["cholesterol"].apply(lambda x: 1 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)

# draw heatmap
corr = round(df.corr(), 1)
mask = np.zeros_like(corr)
np.triu_indices_from(mask)
mask[np.triu_indices_from(mask)] = True
sns.axes_style("white")
plt.figure(figsize=(14, 14))
fig = sns.heatmap(
    corr, annot=True, fmt=".2g", linewidths=0.5, mask=mask, square=True, center=0.08
)
fig = fig.get_figure()
fig.savefig("medical-heatmap.png")
