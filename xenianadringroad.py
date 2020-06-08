n, m = map(int, input().split())
arr = [int(x) for x in input().split()]

houses = [x for x in range(1, n+1)]

ans, loc = 0, 1

for i in range(0, m):
    if(arr[i] >= loc):
        ans += arr[i] - loc
    else:
        ans += n - loc + arr[i]
    loc = arr[i]


print(ans)
