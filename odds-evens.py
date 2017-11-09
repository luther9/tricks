#!/usr/bin/python3


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
