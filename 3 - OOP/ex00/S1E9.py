from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a character with a first name and alive status."""

        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Set the character's alive status to False."""
        pass


class Stark(Character):
    """Class representing a Stark character, inheriting from Character."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Stark character with a first name and alive status."""

        super().__init__(first_name, is_alive)

    def die(self):
        """Set the Stark character's alive status to False."""

        self.is_alive = False
