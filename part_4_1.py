"""
Write a unit test for the function merge_dicts.

It should be possible to run the test in this file using PyTest
eg.
    pytest part_4_1.py

"""


def merge_dicts(src: dict, dest: dict):
    """
    Merge the source dict into the destination dict.
    """
    for key, value in src.items():
        if isinstance(value, dict):
            # Get node or create one
            node = dest.setdefault(key, {})
            if node is None:
                dest[key] = value
            else:
                merge_dicts(value, node)
        else:
            dest[key] = value

    return dest

def test_merge_dicts():
    """Your code here"""
