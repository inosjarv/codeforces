n = int(input())
seq = [int(x) for x in input().split()]

max_val = max(seq)
frac_total = 0

if(max_val == 0):
    print(format(0, '.12f'))

else:
    for value in seq:
        frac_total += (value/max_val)
    result = (frac_total*max_val)/n

    print(format(result, '.12f'))
