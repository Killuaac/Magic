class Point:

    def __new__(cls, *args, **kwargs):
        print('method new')
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 8)
print(p.x)
