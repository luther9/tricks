#!/usr/bin/python3

from compdescriptors import Delegate


class Int:
    __slots__ = '_data', '_former'
    __str__ = Delegate('_data')

    def __init__(self, data=0, _former=None):
        self._data = data
        # This variable is set by __pos__ and __neg__ to tell us if we're in an
        # increment or decrement.
        self._former = _former

    def __pos__(self):
        if self._former is None:
            return type(self)(self._data, self)
        self._former._data += 1

    def __neg__(self):
        if self._former is None:
            return type(self)(-self._data, self)
        self._former._data -= 1

    def __int__(self):
        return self._data


# This list is incomplete and untested, but hopefully you get the idea. These
# methods need to reset _former.
for name in 'add sub mul matmul truediv floordiv mod divmod pow lshift rshift and xor or'.split():
    method = f'__{name}__'

    def func(self, *args):
        self._former = None
        return type(self)(getattr(self._data, method)(*(int(a) for a in args)))

    setattr(Int, method, func)


def main():
    i = Int(10)
    print(i)
    print(+i)
    print(-i)
    ++i
    print(i)
    --i
    print(i)


main()
