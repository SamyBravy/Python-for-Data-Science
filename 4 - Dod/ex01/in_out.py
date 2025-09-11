def square(x: int | float) -> int | float:
    """Returns the square of x."""

    if isinstance(x, (int, float)):
        return float(x**2)
    else:
        print("Error: Input must be an integer or float.")
        return None


def pow(x: int | float) -> int | float:
    """Returns the result of x raised to the power of x."""

    if isinstance(x, (int, float)):
        return x**x
    else:
        print("Error: Input must be an integer or float.")
        return None


def outer(x: int | float, function) -> object:
    """
    Returns a closure that applies the given function to x
    each time it's called.
    """

    if not isinstance(x, (int, float)):
        print("Error: First argument must be an integer or float.")
        return None
    if not callable(function):
        print("Error: Second argument must be a callable function.")
        return None

    count = x

    def inner() -> float:
        """Applies the function to count and updates count."""

        nonlocal count
        count = function(count)
        return count
    return inner
