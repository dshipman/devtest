"""
Write a short docstring for the function below,
so that other people reading this code can quickly understand what this function does.

You may also rename the functions if you can think of clearer names.
"""

def step_function_maker(start_time, end_time, value):
    def my_function(time):
        if start_time <= time <= end_time:
            y = value
        else:
            y = 0.0
        return y

    return my_function
