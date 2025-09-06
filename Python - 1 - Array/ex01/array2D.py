import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints the shape of the array, slices it
    and returns the sliced array as a list
    """
    if not isinstance(start, int) or not isinstance(end, int):
        print("Error: start and end must be integers")
        return []
    if not isinstance(family, list):
        print("Error: family must be a list")
        return []
    if not all(isinstance(i, list) for i in family):
        print("Error: family must be a 2D list")
        return []
    if not all(len(i) == len(family[0]) for i in family):
        print("Error: all rows in family must have the same length")
        return []

    array = np.array(family)
    print(f"My shape is : {array.shape}")

    new_array = array[start:end]
    print(f"My new shape is : {new_array.shape}")
    return new_array.tolist()
