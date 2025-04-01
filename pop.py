

import bytearray

class ListPop:
    def __init__(self, lst):
        self.lst = bytearray(lst)

    def pop(self, n):
        if not self.lst:
            raise IndexError("Cannot pop from an empty list")
        if n < 0 or n >= len(self.lst):
            raise IndexError("Index out of range")
        element = bytearray([self.lst[n]])
        self.lst = bytearray(self.lst[:n] + self.lst[n+1:])
        return element