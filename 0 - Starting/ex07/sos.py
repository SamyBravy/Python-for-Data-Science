import sys


def toMorse(c):
    """Convert a character to Morse code."""

    NESTED_MORSE = {
                        " ": "/ ",
                        "A": ".- ",
                        "B": "-... ",
                        "C": "-.-. ",
                        "D": "-.. ",
                        "E": ". ",
                        "F": "..-. ",
                        "G": "--. ",
                        "H": ".... ",
                        "I": ".. ",
                        "J": ".--- ",
                        "K": "-.- ",
                        "L": ".-.. ",
                        "M": "-- ",
                        "N": "-. ",
                        "O": "--- ",
                        "P": ".--. ",
                        "Q": "--.- ",
                        "R": ".-. ",
                        "S": "... ",
                        "T": "- ",
                        "U": "..- ",
                        "V": "...- ",
                        "W": ".-- ",
                        "X": "-..- ",
                        "Y": "-.-- ",
                        "Z": "--.. ",
                        "0": "----- ",
                        "1": ".---- ",
                        "2": "..--- ",
                        "3": "...-- ",
                        "4": "....- ",
                        "5": "..... ",
                        "6": "-.... ",
                        "7": "--... ",
                        "8": "---.. ",
                        "9": "----. "
                    }
    return NESTED_MORSE[c.capitalize()]


def main():
    """Main function that prints the Morse code of the input string."""

    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    for c in sys.argv[1]:
        if not c.isalnum() and c != ' ':
            print("AssertionError: the arguments are bad")
            sys.exit(1)

    for c in sys.argv[1]:
        print(toMorse(c), end='')
    print()


if __name__ == "__main__":
    main()
