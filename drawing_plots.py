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

#figure, axis = plt.subplots(len(columns), len(rows)) 

# filtered_df = df[df["gt_corners"].isin([columns[j]])]
# filtered_df.hist(column=rows[i])



for iteration in columns: 
    filtered_df = df[df["gt_corners"].isin([iteration])].filter(items=rows)
    filtered_df.hist()
    # plt.figure(figsize=(10,5))
    plt.show()

# i=0
# j=0

# for i in range(0, len(columns)):
#     for j in range(0, len(rows)):
#         axis[i, j].hist(df[df["gt_corners"].isin([columns[j]])])
#         axis[i, j].set_title(columns[i] + rows[j]) 



