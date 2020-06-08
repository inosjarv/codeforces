n, L = map(int, input().split())
arr = [int(x) for x in input().split()]
arr.sort()

x = arr[0] - 0
y = L - arr[-1]

r = max(x, y) * 2

for i in range(1, n):
    r = max(r, arr[i] - arr[i-1])

print(format(r/2, '.12f'))
