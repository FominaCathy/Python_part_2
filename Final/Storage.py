from collections import defaultdict


class Storage:
    index = 0

    def __init__(self):
        self.storage = defaultdict(list)

    def __str__(self):
        txt = '\n'.join((f'{key}: {value}' for key, value in self.storage.items()))
        return txt

    def __call__(self, value):
        self.storage[type(value)].append(value)

    def __iter__(self):
        return self

    def __next__(self):
        spam = [value for value in self.storage.values()]
        while self.index < len(spam):
            self.index += 1
            return spam[self.index - 1]

        raise StopIteration




class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.second < self.stop:
            self.first, self.second = self.second, self.second + self.first
            if self.first >= self.start:
                return self.first
        raise StopIteration


if __name__ == "__main__":
    s = Storage()
    s(42)
    s(True)
    s({'ex': 'execute'})
    s('hello kitty')

    # print(s)

    fib = Fibonacci(20, 100)
    for num in fib:
        print(num)

    for item in s:
        print(item)
