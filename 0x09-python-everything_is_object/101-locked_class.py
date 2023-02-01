#!/usr/bin/python3
""" LockedClass
"""


class LockedClass:
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("Cannot set attribute")
        super().__setattr__(name, value)

