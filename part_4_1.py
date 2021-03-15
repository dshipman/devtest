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
    """
    This tests a wide variety of functionality and should actually be several unit tests,
    but it's just one since that's what the question asks for...
    There is also untested functionality still in there.
    """

    # Test basic functionality
    src = {'a': 0, 'b': 1}
    dest = {'b': 2, 'c': 3}

    merge_dicts(src, dest)

    # Check for all keys
    assert(set(dest) == set(['a', 'b', 'c']))

    # Check that values have been propagated to existing keys
    assert(dest['b'] == src['b'])

    # Check new keys have been created with correct values
    assert(dest['a'] == src['a'])

    ###
    # This part should be in a different test, but there's a bug in the original function
    # and we want to test it...

    src = {'nested_src': {'a': 0, 'b': 1}}
    dest = {'nested_src': 0}

    merge_dicts(src, dest)

    # Don't even know what to assert here since it's hard to interpret the original intention 
    # of merge_dicts here...
