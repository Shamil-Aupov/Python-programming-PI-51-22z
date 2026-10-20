n = int(input())

product = 1
for _ in range(n):
    x = int(input())
    if x != 0:         
        product *= x

print(product)