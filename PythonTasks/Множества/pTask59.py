m = int(input())
dishes = [input() for _ in range(m)] 

cooked = set()
n = int(input())
for _ in range(n):
    cooked.update(input().split())

for d in dishes:
    if d not in cooked:
        print(d)