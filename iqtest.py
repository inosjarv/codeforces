n = int(input())
seq = [int(x) for x in input().split()]

even_index, even_count, odd_index, odd_count = 0, 0, 0, 0

for i, value in enumerate(seq):
    if(value % 2 == 0):
        even_index = i
        even_count += 1
    elif(value % 2 == 1):
        odd_count += 1
        odd_index = i

if(even_count == 1):
    print(even_index + 1)
else:
    print(odd_index + 1)
