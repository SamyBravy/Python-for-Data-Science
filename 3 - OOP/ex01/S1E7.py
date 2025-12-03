from S1E9 import Character


class Baratheon(Character):
    """Class representing a Baratheon character."""

    def __init__(self, first_name, is_alive=True):
        """Initializes a Baratheon character with specific attributes."""

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return a string representation of the Baratheon character."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of the Baratheon character."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Set the Baratheon character's alive status to False."""

        self.is_alive = False


class Lannister(Character):
    """Class representing a Lannister character."""

    def __init__(self, first_name, is_alive=True):
        """Initializes a Lannister character with specific attributes."""

        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return a string representation of the Lannister character."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of the Lannister character."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Set the Lannister character's alive status to False."""

        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Static method to create a Lannister character."""

        return cls(first_name, is_alive)
