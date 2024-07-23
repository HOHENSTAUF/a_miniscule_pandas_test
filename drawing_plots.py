import numpy as np
import pandas as pd #add
import matplotlib.pyplot as plt
import json
#class plot_drawer

df = pd.read_json("./data/deviations.json")


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



# for iteration in columns: 
#     filtered_df = df[df["gt_corners"].isin([iteration])].filter(items=rows)
#     plt.figure(figsize=(10,7))
#     filtered_df.hist()
#     plt.show()  




filtered_df = df[df["gt_corners"].isin([columns[0]])].filter(items=rows)
#plt.figure(figsize=(10,7))
#plt.hist(filtered_df[rows[2]])


#plt.figure(figsize=(10,7))

fig, axs = plt.subplots(3, 3, layout="constrained")
fig.suptitle('deviation histograms for corners = ' + str(columns[0]) + '\n',
          fontweight = "bold")
fig.set_size_inches(13, 10)

fig.supxlabel('Deviation value')
fig.supylabel('Frequency')

# fig.text(0.5, 0.04, 'Deviation value', ha='center', va='center')
# fig.text(0.06, 0.5, 'Frequency', ha='center', va='center', rotation='vertical')


for i in range(3):
    for j in range(3):
       axs[i, j].hist(filtered_df[rows[3*i+j]], bins=25)
       axs[i, j].set_title('\n\n'+ str(rows[3*i+j]), fontfamily = "serif" , loc = "left" , fontsize = "medium")
       


# axs[0, 0].hist(filtered_df[rows[2]])
# axs[0, 0].set_title('A single plot')
# axs[0, 1].hist(filtered_df[rows[3]])
# axs[0, 1].set_title('A single plot')
plt.show()


# i=0
# j=0

# for i in range(0, len(columns)):
#     for j in range(0, len(rows)):
#         axis[i, j].hist(df[df["gt_corners"].isin([columns[j]])])
#         axis[i, j].set_title(columns[i] + rows[j]) 





class drawing_plots:


    def draw_plots():
        
        #draw comparison plots:
        ## histograms for corner number
        ## histograms for gt/rb corners
        ## 

        #saves as files
        #return paths
        return 0