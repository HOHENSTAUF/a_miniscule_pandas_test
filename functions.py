import numpy as np
import pandas as pd #add
import matplotlib.pyplot as plt
import json

class drawing_plots:

    def draw_plots(dataframe_input):
        
        df = dataframe_input
       # df = pd.read_json("./data/deviations.json") #read from input
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
        paths = []

        fig, ax1 = plt.subplots()
        ax1.hist([df['gt_corners'],df['rb_corners']])
        file_name = './corners_histogram'
        plt.savefig(file_name)       #draws a histogram for corners gt/predicitons to compare
        paths.append(file_name)
       

        for iteration in columns:
            #df slice for a certain corner number
            filtered_df = df[df["gt_corners"].isin([iteration])].filter(items=rows)

            #figure properties
            fig, axs = plt.subplots(3, 3, layout="constrained")
            fig.suptitle('deviation histograms for corners = ' + str(iteration) + '\n',
                    fontweight = "bold")
            fig.set_size_inches(13, 10)
            fig.supxlabel('Deviation value')
            fig.supylabel('Frequency')


            for i in range(3):
                for j in range(3):
                    axs[i, j].hist(filtered_df[rows[3*i+j]], bins=25)
                    axs[i, j].set_title('\n\n'+ str(rows[3*i+j]), fontfamily = "serif" , loc = "left" , fontsize = "medium")

            #here the function saves its drawings to the active folder + path to the path array
           # plt.show()
            file_name = './deviations histograms for ' + str(iteration) + ' corners.png'
            plt.savefig(file_name)
            paths.append(file_name)


        #and here it returns paths
        return paths

#print(drawing_plots.draw_plots())