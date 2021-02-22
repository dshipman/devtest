"""
Using pandas:
    - load the CSV file specified by CSV_FILE
    - using the data in the file, create a plot where 
        - the x axis is time (ascending)
        - the y axis is the cumulative sum of daily infections for all people aged over 20
    - save the plot to the file "part_2_4.png"

An example of a "cumulative sum":
    input: [1, 2, 1, 1, 2, 3, 1, 1]
    cumulative sum: [1, 3, 4, 5, 7, 10, 11, 12]

You don't need to get fancy with labelling plot axes or adding titles or anything like that.
If you cannot figure out how to do all of this, then plot something else.
"""
import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "data/report_2_3.csv"  # Same CSV file as the last question

# Your code goes here
