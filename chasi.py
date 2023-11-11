class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Ты шо дурачок?')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = self.seconds // 60 % 60
        h = self.seconds // 3600 % 24
        return f'{h} : {m} : {s}'

    def __eq__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Нужно вывести целое число')
        # if isinstance(other, int):
        #     other = other
        # else:
        #     other = other.seconds
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc

    def __lt__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Нужно вывести целое число')
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Ну ты и дурачоок')
        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds + sc)


cl = Clock(86400)
print(cl.get_time())
cl = cl + 20
print(cl.get_time())