n = int(input())
seq = [int(x) for x in input().split()]

best, counter, last = 0, 0, 0

for x in seq:
    if x < last:
        best = max(best, counter)
        counter = 0
    counter += 1
    last = x

print(max(best, counter))
