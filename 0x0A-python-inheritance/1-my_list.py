#!/usr/bin/python3

"""make inherited list."""


class Mylist(list):
    """write a class mylist that inherites from list."""

    def print_sorted(self):
        """print a list in sorted ascending order."""
        print(sorted(self))
