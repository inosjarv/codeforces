n = int(input())
arr = [int(x) for x in input().split()]

maxVal = arr[0]
maxValIdx = 0
minVal = arr[n-1]
minValIdx = n-1

for i in range(n):
    if arr[i] > maxVal:
        maxVal = arr[i]
        maxValIdx = i

    if arr[i] <= minVal:
        minVal = arr[i]
        minValIdx = i

swaps = maxValIdx
swaps += (n - 1) - minValIdx

if maxValIdx > minValIdx:
    swaps -= 1

print(swaps)
