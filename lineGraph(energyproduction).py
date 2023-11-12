#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:36:32 2023

@author: saideepak
"""

# Import the pandas library for data manipulation and analysis
import pandas as pd

# Import the Matplotlib library for creating plots and visualizations
import matplotlib.pyplot as plt

# Import the NumPy library for numerical computations
import numpy as np

# Reading data from excel and storing in energyProduction DataFrame
energyProduction = pd.read_excel("Data/energyproduction.xlsx")

# creating function for cleaning DataFrame


def cleaning(data):
    """
    This function takes one parameter and
    performs slicing operation on unwanted data,
    which affects accessing data harder

    Parameter: (data) type is DataFrame

    Returns: (data)type is DataFrame
    """
    data = data.iloc[1:-4, 0:-3]
    data = data.round()
    return data

# creating function for adding new index


def newIndex(data):
    """
    This function takes one parameter and
    performs column on row to evade Warning,
    then set copied column as Index,
    later changes name of Index,
    and drops the row, which is no longer used.

    Parameter: (data) type is DataFrame.

    Returns: (data)type is DataFrame.
    """
    index = data.iloc[:, 0]
    indexCopy = index.copy()
    indexCopy.iloc[0] = "Name"
    data = data.set_index(indexCopy)
    data.index.name = "Name"
    data = data.drop("Unnamed: 0", axis=1)
    return data

# creating function for replacing column


def newColumn(data):
    """
    This function takes one parameter and
    performs copy on row to evade Warning,
    then set copied row as column name,
    later changes name of Column names,
    and drops the row, which is no longer used.

    Parameter: (data) type is DataFrame.

    Returns: (data)type is DataFrame.

    """
    col = data.loc["Name"]
    colcopy = col.copy()
    colcopy = colcopy.astype(int)
    data = data.rename(columns=colcopy)
    data = data.drop("Name", axis=0)
    return data


# calling cleaning, newIndex,newColumn functions
energyProduction = cleaning(energyProduction)
energyProduction = newIndex(energyProduction)
energyProduction = newColumn(energyProduction)

print(energyProduction.head(5))

# Create a new figure
plt.figure(figsize=(12, 6), dpi=310)

# Plot the data as a line graph
# Plotting World, blue color, solid line
plt.plot(
    energyProduction.columns,
    energyProduction.loc["World"],
    "b",
    label="World")
# Plotting G7, black color, dashed line
plt.plot(
    energyProduction.columns,
    energyProduction.loc["G7"],
    "k--",
    label="G7")
# Plotting BRICS, red color, dotted line
plt.plot(
    energyProduction.columns,
    energyProduction.loc["BRICS"],
    "r:",
    label="BRICS")
# Plotting European Union, yellow color, dash-dot line
plt.plot(
    energyProduction.columns,
    energyProduction.loc["European Union"],
    "y-.",
    label="EU")

# Add labels and a title
plt.xlabel("Time Interval (Year 1990-2020)")
plt.ylabel("Energy Production (Mtoe)")
plt.title("Total Energy Production")

# Customize the plot
plt.grid(True)
plt.xlim(1989, 2021)

# Add a legend to the graph
plt.legend()

# Saving and Showing graph
plt.savefig("Graph/energyproduction.png", dpi=310)
plt.show()
