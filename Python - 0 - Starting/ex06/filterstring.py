import sys
from ft_filter import ft_filter


def main():
    """Main function to filter strings based on length."""
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    for c in sys.argv[1]:
        if not c.isprintable() or c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            print("AssertionError: the arguments are bad")
            sys.exit(1)

    try:
        my_list = sys.argv[1].split()
        n = int(sys.argv[2])
    except Exception:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    my_list = ft_filter(lambda elem: len(elem) > n, my_list)
    print(list(my_list))


if __name__ == "__main__":
    main()
