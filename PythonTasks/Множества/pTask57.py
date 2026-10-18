n = int(input())
counts = {}

for _ in range(n):
    s = input()
    counts[s] = counts.get(s, 0) + 1  

total = 0
for c in counts.values():
    if c > 1:
        total += c           

print(total)