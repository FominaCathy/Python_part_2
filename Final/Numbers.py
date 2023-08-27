class Numbers:

    def __init__(self, num):
        self.num = num

    def __call__(self, num):
        return num // 5


n = Numbers(45)
print(callable(Numbers))

print(n.num)
print(n(45))
