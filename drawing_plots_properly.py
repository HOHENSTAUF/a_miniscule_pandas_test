import numpy as np
import pandas as pd #add
import matplotlib.pyplot as plt
import json



# Number of variables wanted
num_variables = 16
[
    "mean",
    "max",
    "min",
    "floor_mean",
    "floor_max",
    "floor_min",
    "ceiling_mean",
]

# Initialize the list that will contains our variable parameters
columns = []
means = []
stds = []

# Generate random data for each variable
for i in range(num_variables):
    
    # Assign a name for each variable
    column_name = f"Variable_{i+1}" # Variable_1, Variable_2, etc
    columns.append(column_name)
    
    # Generate random mean and standard deviation for each variable
    mean = np.random.uniform(0, 100)
    std = np.random.uniform(5, 100)
    means.append(mean)
    stds.append(std)
    
# Generate random data for the DataFrame
data = np.random.normal(loc=means, scale=stds, size=(1000, num_variables))

# Create the DataFrame
df = pd.DataFrame(data, columns=columns)

json_string = '{"name":"Rupert", "age": 25, "desig":"developer"}' #here will be pandas file instead

#class plot_drawer

with open('.\data\data.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)



# data polishiing



# Generating categorical variable with 16 different modalities
categories = df['gt_corners'].unique() #добавить категории по парам значений потом

# size = 10
# categorical_data = np.random.choice(categories, size=size)
# continuous_data = np.random.normal(loc=10, scale=5, size=size)

# # Creating pandas DataFrame
# df = pd.DataFrame({
#     'Continuous_Variable': continuous_data,
#     'Categorical_Variable': categorical_data
# })




# Create a figure and 16 subplots (one for each category)
#fig = fig.figure
fig, axs = plt.subplots(9, 4, figsize=(8, 8))
fig.suptitle('Histograms for Each Deviation by corner number', fontsize=16)


# Flatten the axs array to make it easier to iterate over
# axs = axs.flatten()

# Get a list of (16) distinct colors from the tab20 colormap
# colors = plt.cm.tab20.colors[:num_histograms]

# Iterate over each category and plot the histogram
for i, category in enumerate(categories):
    category_data = df[df['gt_corners'] == category]['mean']
    axs[i].hist(category_data, bins=15, alpha=0.7, edgecolor="black", color=colors[i]) #axs[i] is a numplot and not a df thing
    axs[i].set_title(category, fontsize = 7)
    axs[i].set_xlabel('Value', fontsize = 7)
    axs[i].set_ylabel('Frequency', fontsize = 7)

# Adjust the layout and display the plot
plt.tight_layout()
plt.show()