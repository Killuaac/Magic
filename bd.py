class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        print('Hello World')
        DataBase.__instance = None

    def connect(self):
        print(f'соединение БД: {self.user} {self.psw} {self.port}')

    def close(self):
        print(f'соединение разорвано')

    def read(self):
        print(f'чтение данных')

    def write(self, data):
        print(f'Записываем данные {data}')


db = DataBase('user1', 'psw1', '8000')
db2 = DataBase('user1', 'psw1', '8000')
db.connect()
print(db)
print(db2)
