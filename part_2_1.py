"""
Fix up this code so that it is well formatted (eg. PEP 8 and similar good
practices).
"""

import random


def print_average():
    """
    Prints the average of a random list 100 times
    """
    for i in range(100):
        values = [random.random() for item in range(20)]

        average = sum(values)/len(values)
        print(f"The average of the random list is {average}")

print_average()
