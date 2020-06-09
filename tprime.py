n = int(10**6)
s = list(range(3, n + 1, 2))
primes, i, v = [2], 0, 3
slen = len(s)
while v < n:
    if s[i]:
        primes.append(s[i])
        j = i + v
        while j < slen:
            s[j] = 0
            j += v
    i += 1
    v = 2 * i + 3
print(primes[:10])
input()
for x in map(int, input().split()):
    if x**0.5 in primes:
        print('YES')
    else:
        print('NO')
