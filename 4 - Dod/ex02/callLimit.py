from typing import Any


def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called."""

    if not isinstance(limit, int) or limit < 0:
        print("Error: Argument must be a non-negative integer.")
        return None

    count = 0

    def callLimiter(func):
        """Returns a wrapper function that limits calls to func."""

        if not callable(func):
            print("Error: Argument must be a callable function.")
            return None

        def limit_function(*args: Any, **kwds: Any):
            """Wrapper function that enforces the call limit."""

            nonlocal count
            if count < limit:
                count += 1
                return func(*args, **kwds)
            else:
                print(f"Error: <function '{func.__name__}' at 0x{id(func):x}>\
                      call too many times")

        return limit_function

    return callLimiter
