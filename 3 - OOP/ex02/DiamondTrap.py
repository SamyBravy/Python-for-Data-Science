from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A class representing a King, inheriting from Baratheon and Lannister."""

    def __init__(self, first_name):
        """
        Initialize a King with a first name,
        inheriting from Baratheon and Lannister.
        """
        super().__init__(first_name)

    @property
    def eyes(self):
        """Get the eyes of the King."""

        return self._eyes

    @eyes.setter
    def eyes(self, value):
        """Set the eyes of the King."""

        self._eyes = value

    @property
    def hairs(self):
        """Get the hairs of the King."""

        return self._hairs

    @hairs.setter
    def hairs(self, value):
        """Set the hairs of the King."""

        self._hairs = value

    def get_eyes(self):
        """Get the eyes of the King through the property."""

        return self.eyes

    def set_eyes(self, value):
        """Set the eyes of the King through the property."""

        self.eyes = value

    def get_hairs(self):
        """Get the hairs of the King through the property."""

        return self.hairs

    def set_hairs(self, value):
        """Set the hairs of the King through the property."""

        self.hairs = value
