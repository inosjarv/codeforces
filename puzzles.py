n, m = map(int, input().split(" "))
arr = map(int, input().split(" "))
diff = 10000
arr = sorted(arr)

for k, v in enumerate(arr):
    if k+n-1 < len(arr) and arr[k+n-1]-arr[k] < diff:
        diff = arr[k+n-1]-arr[k]
print(diff)
