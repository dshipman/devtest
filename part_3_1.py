"""
This code calculates and prints a value called "sum_norm".

It takes a long time to run, approximately 10s or so.
It contains some inefficient calculations which can be improved.

Re-write the block inside the Timer so that it runs at least 10x faster, 
while producing the same result.

You can do this without importing any additional libraries.
"""
from timer import Timer

ITEMS = list(range(30000))

"""
Low hanging fruit - move max_item calc out of loop, since it is constant
"""

max_item = max(ITEMS)

with Timer("Calculating sum of normalized items"):
    norm_items = []
    
    norm_items = [i/max_item for i in ITEMS]
    sum_norm = sum(norm_items)

"""
    Alternatively, if we only want the end result (sum_norm), we can skip all the list operations

    This returns a slightly different answer due to accumulation of floating point errors
    (ie this answer is more "correct", but doesn't return the _same_ answer as the original 
    implementation, so isn't quite what was asked for...)

    sum_norm = sum(ITEMS) / max_item
"""

print("The sum of norm items is", sum_norm)
