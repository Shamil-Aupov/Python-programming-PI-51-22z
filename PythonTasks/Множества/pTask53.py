first = []
while True:
    s = input()
    if s == "":
        break
    first.append(s)

second = set()
while True:
    s = input()
    if s == "":
        break
    second.add(s)

res = []
for x in first:     
    if x in second and x not in res:
        res.append(x)

print(" ".join(res) if res else "EMPTY")