import bcrypt
 
class Login:

    def __init__(self, name, surname, login):
        self.name = name # Имя
        self.surname = surname # Фамилия
        self.login = login # Логин

    def info(self):
        print(f"Ваши имя: {self.name}",
                f"/n ваша фамилия: {self.surname}",
                f"/n ваш логин: {self.login}")

person1 = Login(1, 2, 3)
person1.info()

class Autorization:

    def hashing(self, password, hash_algoritm, is_hashed):
        self.password = password
        self.hash_algoritm = hash_algoritm
        self.is_hashed = is_hashed

    def info(self):

        print(f"Ваш пароль: {self.password}",
                f"/n алгоритм хэширования: {self.hash_algoritm}",
                f"/n хэшированный пароль: {self.is_hashed}")

    def hashing_pass(self):
 
        # Declaring our password
        password = b'GeekPassword'
        
        # Adding the salt to password
        salt = bcrypt.gensalt()
        # Hashing the password
        hashed = bcrypt.hashpw(password, salt)
        
        # printing the salt
        print("Salt :")
        print(salt)
        
        # printing the hashed
        print("Hashed")
        print(hashed)