class Test:
    def __repr__(self):
        return 'obj test'

    def __str__(self):
        return 'test str'

    def __bool__(self):
        return 2 < 6


t = Test()
print(t)
