import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random string of 15 lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class representing a student with automatic id and login generation."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Generates the login after initialization."""

        self.login = self.name[0] + self.surname
