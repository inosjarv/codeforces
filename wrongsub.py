n, k = map(int, input().split())
cnt = 0
for i in range(k):
    modulo = int(n % 10)

    if(modulo == 0):
        n = int(n/10)

    if(modulo > 0):
        n -= 1

print(n)
