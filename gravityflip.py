n = int(input())
seq = [int(x) for x in input().split()]

print(' '.join(str(e) for e in sorted(seq)))
