n, k = map(int, input().split())
mid = (n + 1) // 2

if(k <= mid):
    print(2*k-1)
else:
    print((k - mid)*2)
