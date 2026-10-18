first = -1
i = 0

while True:
    s = input()
    if s == "СТОП":
        break
    i += 1
    if first == -1 and "кот" in s.lower():
        first = i

print(first)