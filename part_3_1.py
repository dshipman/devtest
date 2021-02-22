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

with Timer("Calculating sum of normalized items"):
    norm_items = []
    for i in ITEMS:
        max_item = max(ITEMS)
        norm_item = i / max_item
        norm_items.append(norm_item)
        sum_norm = sum(norm_items)

print("The sum of norm items is", sum_norm)
