"""
Using pandas:
    - load the CSV file specified by CSV_FILE
    - using the data in the file, create a plot where 
        - the x axis is time (ascending)
        - the y axis is the number of daily infections (per age group)
    - save the plot to the file "part_2_3.png"

You don't need to get fancy with labelling plot axes or adding titles or anything like that.
If you cannot figure out how to do all of this, then plot something else.
"""

"""
Reviewers: Please note.  This code doesn't run directly under the virtual environment (from part1) 
as installed on Windows due to the current matplotlib version being buggy, but works perfectly 
well in a number of my other environments.

I'm going to assume you're testing my python coding ability, rather than my ability to wrestle with
package management systems

In a production environment, package versions should be locked, to avoid precisely this sort of situation
"""


import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "data/report_2_3.csv"

# Your code goes here

df = pd.read_csv(CSV_FILE)

df = df.set_index('time')

age_groups = df['age'].unique()

new_df = pd.DataFrame()
for ag in age_groups:
    new_df['infections%i'%ag] = df['daily_infections'][df['age']==ag]

plot = new_df.plot()

plot.figure.savefig('part_2_3.png')
