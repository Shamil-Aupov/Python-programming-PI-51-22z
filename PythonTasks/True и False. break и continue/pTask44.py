count = 0
first = -1
i = 0

while True:
    s = input()
    if s == "СТОП":
        break
    i += 1
    if "кот" in s.lower():
        count += 1
        if first == -1:
            first = i

print(count)
print(first)