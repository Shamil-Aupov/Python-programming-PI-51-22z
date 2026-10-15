pwd = input()
pwd2 = input()

if len(pwd) < 8:
    print("Слишком короткий!")
elif pwd != pwd2:
    print("Пароли не совпадают!")
else:
    print("OK")