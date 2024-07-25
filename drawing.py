import numpy as np
import pandas as pd #add
import matplotlib.pyplot as plt
import json

class drawing_plots:

    
    def draw_plots(df: pd.core.frame.DataFrame):

        try:

            #df = pd.read_json("./data/deviations.json") #read from input
            corners = df['gt_corners'].unique() 
            # deviation_cols = df.corners[3:]
            deviation_cols = [
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
        

            for corner in corners:
                #df slice for a certain corner number

                # df.loc[], df.iloc[], ==
                filtered_df = df[df["gt_corners"].isin([corner])].filter(items=deviation_cols)

                #figure properties
                fig, axs = plt.subplots(3, 3, layout="constrained")
                fig.suptitle('deviation histograms for corners = ' + str(corner) + '\n',
                        fontweight = "bold")
                fig.set_size_inches(13, 10)
                fig.supxlabel('Deviation value')
                fig.supylabel('Frequency')


                for i in range(3):
                    for j in range(3):
                        axs[i, j].hist(filtered_df[deviation_cols[3*i+j]], bins=25)
                        axs[i, j].set_title('\n\n'+ str(deviation_cols[3*i+j]), fontfamily = "serif" , loc = "left" , fontsize = "medium")

                #here the function saves its drawings to the active folder + path to the path array
            # plt.show()
                file_name = './deviations histograms for ' + str(corner) + ' corners.png'
                plt.savefig(file_name)
                paths.append(file_name)


            #and here it returns paths
            return paths
        
        except(TypeError):
            raise TypeError("Input Type is not valid")

#print(drawing_plots.draw_plots())

# df = pd.read_json("./data/deviations.json")
# drawing_plots.draw_plots(df)