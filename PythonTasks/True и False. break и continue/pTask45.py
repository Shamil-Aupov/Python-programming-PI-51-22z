a = int(input())
b = int(input())
res = []

for x in range(a, b + 1):
    if x % 3 == 0 and x % 5 == 0:
        res.append("FizzBuzz")
    elif x % 3 == 0:
        res.append("Fizz")
    elif x % 5 == 0:
        res.append("Buzz")
    else:
        res.append(str(x))

print(" ".join(res))