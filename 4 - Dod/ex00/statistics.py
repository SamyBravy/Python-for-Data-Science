from typing import Any


def mean(numbers):
    """Calculate the mean of a list of numbers."""

    return sum(numbers) / len(numbers)


def median(numbers):
    """Calculate the median of a list of numbers."""

    numbers = sorted(numbers)
    length = len(numbers)

    if length % 2 == 1:
        return numbers[length // 2]
    else:
        return mean([numbers[length // 2 - 1], numbers[length // 2]])


def quartile(numbers):
    """Calculate the first and third quartiles of a list of numbers."""

    numbers = sorted(numbers)
    length = len(numbers)

    q1 = float(median(numbers[:length // 2 + (1 if length % 2 == 1 else 0)]))
    q2 = float(median(numbers[length // 2:]))

    return [q1, q2]


def var(numbers):
    """Calculate the variance of a list of numbers."""

    m = mean(numbers)
    return sum((x - m) ** 2 for x in numbers) / len(numbers)


def std(numbers):
    """Calculate the standard deviation of a list of numbers."""

    variance = var(numbers)
    return variance ** 0.5


def check_validity(numbers):
    """Check if the input is a valid list of numbers."""

    if len(numbers) == 0:
        print("ERROR")
        return False

    if not all(type(n) in [int, float] for n in numbers):
        print("ERROR")
        return False

    return True


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Perform statistical operations on a list of numbers
    based on provided keywords.
    """

    for _, op in kwargs.items():
        match op:
            case "mean":
                if not check_validity(args):
                    continue
                print("mean : ", mean(args))
            case "median":
                if not check_validity(args):
                    continue
                print("median : ", median(args))
            case "quartile":
                if not check_validity(args):
                    continue
                print("quartile : ", quartile(args))
            case "std":
                if not check_validity(args):
                    continue
                print("std : ", std(args))
            case "var":
                if not check_validity(args):
                    continue
                print("var : ", var(args))
