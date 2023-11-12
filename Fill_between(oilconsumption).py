#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:04:28 2023

@author: saideepak
"""

# Import the pandas library for data manipulation and analysis
import pandas as pd

# Import the Matplotlib library for creating plots and visualizations
import matplotlib.pyplot as plt

# Import the NumPy library for numerical computations
import numpy as np
# Reading data from excel and storing in oilConsumption DataFrame
oilConsumption = pd.read_excel("Data/oilconsumption.xlsx")
# Creating function for cleaning DataFrame


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
# Creating function for adding new index


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
    data.index.name = 'Name'
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
oilConsumption = cleaning(oilConsumption)
oilConsumption = newIndex(oilConsumption)
oilConsumption = newColumn(oilConsumption)
# Create a new figure
plt.figure(figsize=(12, 8))

# Plot the line
plt.plot(oilConsumption.loc["China"], 'b')
# Fill the area between China line and India line with a color
plt. fill_between(
    oilConsumption.columns,
    oilConsumption.loc["China"],
    oilConsumption.loc["India"],
    where=(
        oilConsumption.loc["China"] > oilConsumption.loc["India"]),
    interpolate=True,
    color='blue',
    alpha=0.25,
    label='China')

# Plot the line
plt.plot(oilConsumption.loc["India"], 'g')
# Fill the area between the line and the x-axis with green color
plt. fill_between(
    oilConsumption.columns,
    oilConsumption.loc["India"],
    interpolate=True,
    color='green',
    alpha=0.25,
    label='India')


# Plot the line
plt.plot(oilConsumption.loc["United States"], 'r')
# Fill the area between the United States and China with red color
plt. fill_between(
    oilConsumption.columns,
    oilConsumption.loc["United States"],
    oilConsumption.loc["China"],
    where=(
        oilConsumption.loc["United States"] > oilConsumption.loc["China"]),
    interpolate=True,
    color='red',
    alpha=0.25,
    label='United States')

# Plot the line
plt.plot(oilConsumption.loc["Russia"], 'k')
# Fill the area between Russia line and the x-axis with black color
plt. fill_between(
    oilConsumption.columns,
    oilConsumption.loc["Russia"],
    interpolate=True,
    color='black',
    alpha=0.25,
    label='Russia')

# Add labels and a title
plt.xlabel("Time Interval (Year 1990-2020)")
plt.ylabel("Oil Consumption(Mt)")
plt.title("Total Oil Consumption")

# Add lim and legend
plt.xlim(1989, 2021)
plt.legend()

# Saving and Showing graph
plt.savefig("Graph/oilconsumption.png", dpi=310)
plt.show()
