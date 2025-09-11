class calculator:
    """
    Calculator class that performs basic arithmetic operations
    on a list of numbers.
    """

    def __init__(self, values: list[float]) -> None:
        """Initialize the calculator with a list of numerical values."""

        self.values = values

    def __add__(self, object) -> None:
        """Add a number to each element in the list."""

        for i in range(len(self.values)):
            self.values[i] += object
        print(self.values)

    def __mul__(self, object) -> None:
        """Multiply each element in the list by a number."""

        for i in range(len(self.values)):
            self.values[i] *= object
        print(self.values)

    def __sub__(self, object) -> None:
        """Subtract a number from each element in the list."""

        for i in range(len(self.values)):
            self.values[i] -= object
        print(self.values)

    def __truediv__(self, object) -> None:
        """Divide each element in the list by a number."""

        if object == 0:
            print("Error: Division by zero")
            return

        for i in range(len(self.values)):
            self.values[i] /= object
        print(self.values)
