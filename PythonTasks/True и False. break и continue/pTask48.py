found = False

while True:
    s = input()
    if s == "СТОП":
        break
    if "кот" in s.lower():
        found = True
    if "пёс" in s.lower(): 
        found = False

print("МЯУ" if found else "НЕТ")