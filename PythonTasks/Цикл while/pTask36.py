while True:
    pwd = input()
    pwd2 = input()

    if len(pwd) < 8:
        print("Слишком короткий!")
    elif "123" in pwd:
        print("Содержит 123!")
    elif pwd != pwd2:
        print("Пароли не совпадают!")
    else:
        print("OK")
        break