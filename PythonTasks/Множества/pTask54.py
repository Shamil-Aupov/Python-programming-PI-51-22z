m = int(input())
eng = {input() for _ in range(m)}

n = int(input())
ger = {input() for _ in range(n)}

only_one = eng ^ ger     
print(len(only_one) if only_one else "NO")