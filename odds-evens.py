#!/usr/bin/python3


def odds():
    yield 1
    for i in evens():
        yield i + 1


def evens():
    for i in odds():
        yield i + 1


def test_gen(gen):
    for _ in range(10):
        print(next(gen))


def main():
    test_gen(odds())
    test_gen(evens())


main()
