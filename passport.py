import random


class Passport:
    def __init__(self, first_name, last_name, country,
                 date_of_birth, num_of_passport):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date_of_birth = date_of_birth
        self.num_of_passport = num_of_passport

    def printInfo(self):
        print(f'''
Full name: {self.first_name} {self.last_name}
Date of birth : {self.date_of_birth}
country: {self.country}
passport: {self.num_of_passport}
''')

    def __repr__(self):
        return f'name: {self.first_name} {self.last_name}, {self.num_of_passport}'


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, country,
                 date_of_birth, num_of_passport, visa):
        super().__init__(first_name, last_name, country,
                         num_of_passport, date_of_birth)
        self.visa = visa

    def printInfo(self):
        print(f'''
Full name: {self.first_name} {self.last_name}
Date of birth : {self.date_of_birth}
country: {self.country}
visa: {self.visa}
passport: {self.num_of_passport}
''')


MFC = []
fp = ForeignPassport('Petr', 'Petrov', 'страна Z',
                     '13.10.1996', 12345678, 'China')
MFC.append(fp)
p = Passport('Ivan', 'Ivanov', 'страна Z',
             14.05, 7220222513)
MFC.append(p)
fp.printInfo()
p.printInfo()
print(MFC)
for item in MFC:
    item.printInfo()


