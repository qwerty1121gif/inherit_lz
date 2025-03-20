from safety import Authorization

def main():
    users = [
        Authorization("Alesha", "Arabian", "alesha", "98123892098310238013846819023912487_ALESHA_VZLOMAL_PENTAGON", hash_algorithm="bcrypt"),
        Authorization("Vladislav", "No", "admin", "ne_skazhu", hash_algorithm="bcrypt"),
        Authorization("Denis", "Chestniy", "garlik", "Deniska128585", hash_algorithm="bcrypt"),
        Authorization("Ilya", "Light", "aborigen", "12.03.2007!Ilusha", hash_algorithm="bcrypt"),
        Authorization("Dima", "Belan", "kriptan_unknown", "YAkriptan", hash_algorithm="bcrypt")
    ]

    #Красиво выводим
    for index, user in enumerate(users, 1):
        print(f"\n*** Пользователь {index} ***")
        user.info()
        print(f"Является сотрудником? {'Да' if user.is_employee() else 'Нет'}")
    try:
        hacker = Authorization(
            name="Хакер",
            surname="Злой",
            login="hacker",
            password="pwned",
            hash_algorithm="md5"  # Неподдерживаемый алгоритм
        )
        hacker.info()
    except ValueError as e:
        print(f"\nНепорядок.. {e}")

if __name__ == "__main__":
    main()