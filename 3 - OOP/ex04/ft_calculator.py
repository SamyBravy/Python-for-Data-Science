class calculator:
    """
    Calculator class that performs basic arithmetic operations on vectors.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors."""

        dot = sum(a * b for a, b in zip(V1, V2))
        print("Dot product is:", dot)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate the sum of two vectors."""

        sum = [float(a + b) for a, b in zip(V1, V2)]
        print("Add Vector is :", sum)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate the difference of two vectors."""

        sub = [float(a - b) for a, b in zip(V1, V2)]
        print("Sous Vector is:", sub)
