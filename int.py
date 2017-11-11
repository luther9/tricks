#!/usr/bin/python3

from compdescriptors import Delegate


class Int:
    __slots__ = '_data', '_increment'
    __str__ = Delegate('_data')

    def __init__(self, data=0, _increment=0):
        self._data = data
        # This variable is set by __pos__ and __neg__ to tell us if we're in an
        # increment or decrement.
        self._increment = _increment

    def __pos__(self):
        if self._increment < 1:
            self._increment = 1
            return self
        self._data += 1
        self._increment = 0

    def __neg__(self):
        if self._increment > -1:
            self._increment = -1
            return self
        self._data -= 1
        self._increment = 0

    def __int__(self):
        return self._data


# These methods are untested.
for name in 'add sub mul matmul truediv floordiv mod divmod pow lshift rshift and xor or'.split():
    method = f'__{name}__'

    def func(self, *args):
        self._increment = 0
        return type(self)(getattr(self._data, method)(*(int(a) for a in args)))

    setattr(Int, method, func)


def main():
    i = Int()
    print(i)
    ++i
    print(i)
    --i
    print(i)


main()
