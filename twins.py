name = int(input())
seq = [int(x) for x in input().split()]

seq = sorted(seq, reverse=True)
mid = sum(seq)//2 + 1

total = 0
count = 0

for val in seq:
    total += val
    count += 1
    if(total >= mid):
        break

print(count)
