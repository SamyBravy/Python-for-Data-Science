import numpy as np


def lst_check_int_float(lst):
    """Check if the input is a list of int or float."""
    if not isinstance(lst, list):
        print("Error: Input is not a list")
        return False
    if not all(isinstance(elem, (int, float)) for elem in lst):
        print("Error: all elements in the list should be int or float")
        return False
    return True


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI from height and weight lists."""
    if not lst_check_int_float(height):
        return []
    if not lst_check_int_float(weight):
        return []
    if len(height) != len(weight):
        print("Error: height and weight lists should have the same length")
        return []
    if not all(h > 0 for h in height) or not all(w > 0 for w in weight):
        print("Error: height and weight should be positive numbers")
        return []

    height, weight = np.array(height), np.array(weight)
    return (weight / height**2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check if each BMI value exceeds the given limit."""
    if not isinstance(limit, int):
        print("Error: limit should be an integer")
        return []
    if not lst_check_int_float(bmi):
        return []
    bmi = np.array(bmi)
    return (bmi > limit).tolist()
