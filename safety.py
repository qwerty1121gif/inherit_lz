import bcrypt

class Login:
    employee_logins = ["olga", "alesha", "virus", "sanchez", "sedoy", "darya", 
                      "gomer", "ganton", "zorich", "timur", "aborigen", 
                      "valera", "admin", "paplaviy", "shprotos", "holodok", 
                      "garlik", "molodoy"]  # Все логины маленькими буквами

    def __init__(self, name, surname, login):
        self.name = name
        self.surname = surname
        self.login = login.lower()  # Приводим логин к маленьким буквам

    def info(self):
        print(f"Имя: {self.name}\nФамилия: {self.surname}\nЛогин: {self.login}")

    def is_employee(self):
        return self.login in Login.employee_logins

class Authorization(Login):
    def __init__(self, name, surname, login, password, hash_algorithm="bcrypt"):
        super().__init__(name, surname, login)
        self.password = password
        self.hash_algorithm = hash_algorithm
        self.is_hashed = False

    def info(self):
        if not self.is_hashed:
            self.hashing_pass()
        super().info()  # Вызываем info() из родительского класса
        print(f"Алгоритм хеширования: {self.hash_algorithm}")
        print(f"Хешированный пароль: {self.password}")

    def hashing_pass(self):
        if self.hash_algorithm == "bcrypt":
            password_bytes = self.password.encode("utf-8")
            salt = bcrypt.gensalt()
            self.password = bcrypt.hashpw(password_bytes, salt).hex()
            self.is_hashed = True
        else:
            raise ValueError("Алгоритм не поддрерживается")