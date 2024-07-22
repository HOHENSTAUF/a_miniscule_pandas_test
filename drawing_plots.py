import numpy as np
import pandas as pd #add
import matplotlib.pyplot as plt
import json
#class plot_drawer

with open('.\data\data.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

columns = df['gt_corners'].unique()

rows = [
    "mean",
    "max",
    "min",
    "floor_mean",
    "floor_max",
    "floor_min",
    "ceiling_mean",
    "ceiling_max",
    "ceiling_min",
]

i=0
j = 2

filtered_df = df[df["gt_corners"].isin([columns[j]])]
filtered_df.hist(column=rows[i])
plt.show()