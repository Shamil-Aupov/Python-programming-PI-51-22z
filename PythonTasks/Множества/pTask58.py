m = int(input())
fridge = {input() for _ in range(m)}

n = int(input())
for _ in range(n):
    parts = input().split()
    name = parts[0]                  
    ingredients = set(parts[1:])     
    if ingredients <= fridge:         
        print(name)