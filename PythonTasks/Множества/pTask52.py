n = int(input())
cities = set()

for _ in range(n):
    cities.add(input())

new_city = input()
print("TRY ANOTHER" if new_city in cities else "OK")