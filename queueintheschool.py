n, t = map(int, input().split())
queue = input()
b = [char for char in queue]


while (t > 0):
    i = 0
    while i < (len(b)-1):
        # to check if 'G' is standing behind 'B',If yes thn swap their positions
        if (b[i] == 'B' and b[i+1] == 'G'):
            b[i], b[i+1] = b[i+1], b[i]
            # as i and i+1 as swapped so it vl be 'B' therefore there is a need to swap
            i += 1
        i += 1
    t -= 1

print(''.join(b))
