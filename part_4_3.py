"""
The function `get_noisy_values` is hard to test because the values keep changing
every time you re-run the test.

Re-write `test_get_noisy_values` so that we still test some of the functionality
of `get_noisy_values`, but avoid the issue of tests failing randomly.

There are several acceptable solutions to this problem.

It should be possible to run the test in this file using PyTest
eg.
    pytest part_4_3.py

"""
import numpy as np


def get_noisy_values():
    signal = np.array([1, 2, 3, 4, 5])
    noise = np.random.random(5)
    return signal + noise

def test_get_noisy_values():
    values = get_noisy_values()
    # expected = np.array([1, 2, 3, 4, 5])
    # This will fail most of the time.
    # assert (values == expected).all()
	
	signal = np.array([1, 2, 3, 4, 5])

	assert (values >= signal).all()
	assert (values < signal + 1.0).all()


	values2 = get_noisy_values()

	# Check that randomizer is being random...
	assert(values.sum != values2.sum())
	# Actually kind of a bad test, since it could conceivably fail,
	# but this is vanishingly unlikely, and such a condition could be 
	# regarded as a bug in its own right...
