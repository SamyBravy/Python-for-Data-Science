import sys


class MyFilter:
    def __init__(self, my_list):
        self.my_list = list(my_list)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= len(self.my_list):
            raise StopIteration
        x = self.my_list[self.i]
        self.i += 1
        return x


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    try:
        if function is None:
            my_list = [elem for elem in iterable if elem]
        else:
            my_list = [elem for elem in iterable if function(elem)]
        return MyFilter(my_list)
    except TypeError:
        print("TypeError")
        sys.exit(1)
