class Equipment:

    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return 'sosat'

    def __str__(self):
        return f'{self.name}, {self.make} {self.year}'

    def __le__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError('Ты шо дурачок')
        return self.year <= other.year


class Printer(Equipment):

    def __init__(self, name, make, year, series):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'печатает'

    def __str__(self):
        return f'{self.name}, {self.series}, {self.make}, {self.year}'


class Scanner(Equipment):

    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'сканирует'

    def __str__(self):
        return f'{self.name}, {self.make} {self.year}'


class Xerox(Equipment):

    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'сканирует'

    def __str__(self):
        return f'{self.name}, {self.make} {self.year}'


def allitems(sklad):
    for item in sklad:
        print(item)


def get_items(baza, ename):
    for item in baza:
        if isinstance(item, ename):
            print(item)


sklad = []
e = Equipment('Apple', 'USA', 2022)
sklad.append(e)
s = Equipment('Apple', 'CHINA', 2019)
sklad.append(s)
x = Equipment('Apple', 'USA', 2014)
sklad.append(x)
v = Equipment('Apple', 'GERMAN', 2013)
sklad.append(v)
b = Equipment('Apple', 'JAPAN', 2001)
sklad.append(b)
n = Equipment('DEXP', 'RUSSIA', 1980)
sklad.append(n)
j = Printer('Rus', 'china', 1998, 5000)
sklad.append(j)
t = Xerox('loool', 'Turkey', 998)
sklad.append(t)
get_items(sklad, Equipment)

