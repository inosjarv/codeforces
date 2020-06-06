n, h = map(int, input().split())
seq = [int(x) for x in input().split()]

total_width = 0

for value in seq:
    if(value > h):
        total_width += 2
    else:
        total_width += 1

print(total_width)
