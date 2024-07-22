
import numpy as np
import pandas as pd #add
import matplotlib.pyplot as plt
import json

# Number of variables wanted
parameters = [
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

# Number of histograms to display
num_histograms = 16

# Create a 4x4 grid of subplots to accommodate 16 histograms
num_rows = 4
num_cols = 4

# Create a figure and subplots
fig, axes = plt.subplots(num_rows, num_cols, figsize=(8, 8))

# Flatten the axes array to iterate through subplots easily
axes_flat = axes.flatten()

# Get a list of (16) distinct colors from the tab20 colormap
colors = plt.cm.tab20.colors[:num_histograms]

# Iterate through the DataFrame columns and plot histograms with distinct colors
for i, (column, ax) in enumerate(zip(df.columns, axes_flat)):
    df[column].plot.hist(ax=ax, bins=15, alpha=0.7, color=colors[i], edgecolor='black')
    ax.set_title(f'Histogram of {column}', fontsize = 7)
    ax.set_xlabel(column, fontsize = 7)

# Remove any extra empty subplots if the number of variables is less than 16
if i < num_histograms - 1:
    for j in range(i + 1, num_histograms):
        fig.delaxes(axes_flat[j])

# Adjust layout and display the plot
plt.tight_layout()
plt.show()