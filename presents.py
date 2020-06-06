n, p, d = int(input()), map(int, input().split()), {}
result = ""
for i, v in enumerate(p):
    d[v] = i + 1

for i in range(n):
    result += str(d[i+1]) + " "

print(result)
