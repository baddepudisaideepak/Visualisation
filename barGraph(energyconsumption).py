#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:41:16 2023

@author: saideepak
"""


# Import the pandas library for data manipulation and analysis
import pandas as pd

# Import the Matplotlib library for creating plots and visualizations
import matplotlib.pyplot as plt

# Import the NumPy library for numerical computations
import numpy as np

# Reading data from excel and storing in energyConsumption DataFrame
energyConsumption = pd.read_excel("Data/energyconsumption.xlsx")

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
    data.index.name = "Name"
    data = data.drop("Unnamed: 0", axis=1)
    return data

# Creating function for replacing column


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


# Calling cleaning, newIndex,newColumn functions
energyConsumption = cleaning(energyConsumption)
energyConsumption = newIndex(energyConsumption)
energyConsumption = newColumn(energyConsumption)
# Transpoing energyConsumption, for better view and visualisation
energyConsumption = energyConsumption.T
print(energyConsumption.head())
# Creating years list , which we use in dataExctraction function
years = [1990, 1995, 2000, 2005, 2010, 2015, 2020]


# Creating dataExtraction function
def dataExtraction(data, columnName):
    """
    This function takes Two parameter and

    First we create an empty list,
    using for loop we go through DataFrame,
    then retrive data, and store it in list,
    at the end we return list.

    Parameter: (data) type is DataFrame.
    Parameter: (columnName) type is string.

    Returns: (emptyList)type is list.
    """
    emptyList = []  # empty list

    for i in years:
        l = data[columnName].loc[i]
        emptyList = np.append(emptyList, l)
    return emptyList


# Calling dataExtraction function
BRICS = dataExtraction(energyConsumption, "BRICS")
G7 = dataExtraction(energyConsumption, "G7")
EU = dataExtraction(energyConsumption, "European Union")
OCED = dataExtraction(energyConsumption, "OECD")


def modifyValue(j):
    """
    This function takes one and

    First we copy an years list,
    to not effect "years" in future use.

    using for loop we go through DataFrame,
    then retrive data, and store it in list,
    at the end we return list.

    Parameter: () type is int.

    Returns: (yearsCopy)type is list.
    """
    yearsCopy = years.copy()

    for i in range(len(yearsCopy)):
        if j == 0:
            yearsCopy[i] -= 1
        else:
            yearsCopy[i] += 1
    return yearsCopy


# Create a new figure and axis
fig, axes = plt.subplots(3, 1, figsize=(8, 12), dpi=310)

# Plot the first subplot
cyears = modifyValue(0)  # modifyValue function call
axes[0].bar(cyears, BRICS, width=2, label="BRICS")
cyears = modifyValue(1)  # modifyValue function call
axes[0].bar(cyears, G7, width=2, label="G7")

# Add labels and a title
axes[0].set_xlabel("Time Interval (Year 1990-2020))")
axes[0].set_ylabel("Energy Consumption(Mtoe)")
axes[0].set_title("BRICS Vs G7")

# Add lim and legend
axes[0].set_xlim(1987.5, 2022.5)
axes[0].legend()


# Plot the second subplot
cyears = modifyValue(0)  # modifyValue function call
axes[1].bar(cyears, BRICS, width=2, label="BRICS")
cyears = modifyValue(1)  # modifyValue function call
axes[1].bar(cyears, EU, width=2, label="EU")


# Add labels and a title
axes[1].set_xlabel("Time Interval (Year 1990-2020))")
axes[1].set_ylabel("Energy Consumption(Mtoe)")
axes[1].set_title("BRICS Vs EU")

# Add lim and legend
axes[1].set_xlim(1987.5, 2022.5)
axes[1].legend()


# Plot the third subplot
cyears = modifyValue(0)  # modifyValue function call
axes[2].bar(cyears, BRICS, width=2, label="BRICS")
cyears = modifyValue(1)  # modifyValue function call
axes[2].bar(cyears, OCED, width=2, label="OCED")

# Add labels and a title
axes[2].set_xlabel("Time Interval (Year 1990-2020))")
axes[2].set_ylabel("Energy Consumption(Mtoe")
axes[2].set_title("BRICS Vs OCED")

# Add lim and legend
axes[2].set_xlim(1987.5, 2022.5)
axes[2].legend()

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show  and Save the entire subplot graph
plt.savefig("Graph/energyconsumption.png", dpi=310)
plt.show()
