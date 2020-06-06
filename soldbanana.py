k, n, w = map(int, input().split())
total, i = 0, 1

while(w > 0):
    total += i*k
    i += 1
    w -= 1

if(total < n):
    print(0)
else:
    print(total - n)
