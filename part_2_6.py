"""
Write a short docstring for the function below,
so that other people reading this code can quickly understand what this function does.

You may also rename the functions if you can think of clearer names.
"""


def create_step_function(start_time, end_time, value):
    """
    Create a step function that takes a single input ('time'), and returns <value> if that input is 
    between start_time and end_time (inclusive), otherwise 0.0
    """
    def step_function(time):
        if start_time <= time <= end_time:
            y = value
        else:
            y = 0.0
        return y

    return step_function
