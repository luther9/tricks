#!/usr/bin/python3

"""
Two mutually recursive generators.

This is the equivalent Haskell code:

odds = 1 : map (+ 1) evens
evens = map (+ 1) odds

The Python code is unfortunately longer than two lines.
"""


def odds():
    yield 1
    for i in evens():
        yield i + 1


def evens():
    for i in odds():
        yield i + 1


def main():
    for gen in (odds(), evens()):
        for _ in range(10):
            print(next(gen))


if __name__ == '__main__':
    main()
