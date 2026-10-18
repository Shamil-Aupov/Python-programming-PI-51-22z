n = int(input())
found = False  

for _ in range(n):
    s = input()
    if "кот" in s.lower():
        found = True

print("МЯУ" if found else "НЕТ")