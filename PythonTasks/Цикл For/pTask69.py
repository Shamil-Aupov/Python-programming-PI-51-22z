n = int(input())

divs = [str(i) for i in range(1, n + 1) if n % i == 0]
print(" ".join(divs))