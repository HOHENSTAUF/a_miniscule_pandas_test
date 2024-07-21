
import numpy as np
import pandas as pd #add
import matplotlib.pyplot as plt
import json

json_string = '{"name":"Rupert", "age": 25, "desig":"developer"}' #here will be pandas file instead

#class plot_drawer

with open('.\data\data.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)


#
#reads json file passed as parameter as a pandas dataframe 
#draws plot for comparing different columns 
#saves plots in a folder called “plots” `~`
#returns paths to all plots `~`
def draw_plots(func_input): #<--- json file as pandas dataframe
    new_dataframe = json.loads(func_input)
    print.type(new_dataframe)
    #draw plot
    #save to plots
    #return path to plot
    

with open('.\data\data.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)



# show the dataframe
# bydefault head() show
# first five rows from top
#df.head()

# scatter plot
# df.plot(kind='scatter',
#         x='gt_corners',
#         y='rb_corners',
#         color='red')

# df.hist('floor_mean') #wrong filter make new


for group in df['gt_corners'].unique():
    
    # Filter the dataset on the group
    filtered_df = df[df['gt_corners']==group]
    
    # Add the histogram to the graphic
    filtered_df['floor_min'].hist(figsize=(8, 4))

# Display the plot    
plt.show()


# set the title
#plt.title('ScatterPlot')

# show the plot
plt.show()
#draw_plots(json_string)     #<----works incorrect
    
data_dict = {'name': ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'],
             'age': [20, 20, 21, 20, 21, 20],
             'math_marks': [100, 90, 91, 98, 92, 95],
             'physics_marks': [90, 100, 91, 92, 98, 95],
             'chem_marks': [93, 89, 99, 92, 94, 92]
             }



# ######example
# # creating a data frame object
# df = pd.DataFrame(data_dict)

# # show the dataframe
# # bydefault head() show
# # first five rows from top
# df.head()

# # scatter plot
# df.plot(kind='scatter',
#         x='math_marks',
#         y='physics_marks',
#         color='red')

# # set the title
# plt.title('ScatterPlot')

# # show the plot
# plt.show()
# #####

