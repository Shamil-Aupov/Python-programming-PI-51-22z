m = int(input())

k = int(input())
order = [input() for _ in range(k)] 
common = set(order)

for _ in range(m - 1):
    k = int(input())
    common &= {input() for _ in range(k)} 
for name in order:
    if name in common:
        print(name)