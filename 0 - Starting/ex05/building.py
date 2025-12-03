import sys


def handle_input():
    """Handle input from the user or command line arguments."""

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)

    if len(sys.argv) < 2:
        sys.argv.append("")
    while sys.argv[1] == "":
        print("What is the text to count?")
        try:
            sys.argv[1] = sys.stdin.readline()
        except KeyboardInterrupt:
            print("\nError: KeyboardInterrupt")
            sys.exit(1)

    return sys.argv[1]


def main():
    """Receive a string, count types of characters, and display results."""

    text = handle_input()

    uppers = lowers = puncts = digits = spaces = 0
    for c in text:
        if c.isupper():
            uppers += 1
        elif c.islower():
            lowers += 1
        elif c.isdigit():
            digits += 1
        elif c.isspace():
            spaces += 1
        elif c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            puncts += 1

    print(f"The text contains {len(text)} characters:")
    print(uppers, "upper letters")
    print(lowers, "lower letters")
    print(puncts, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")


if __name__ == "__main__":
    main()
