m = int(input())
library = {input() for _ in range(m)}

n = int(input())
for _ in range(n):
    book = input()
    print("YES" if book in library else "NO")