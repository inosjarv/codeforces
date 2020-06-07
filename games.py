n = int(input())
h, a = list(), list()
number = 0
for i in range(n):
    hi, ai = map(int, input().split())
    h.append(hi)
    a.append(ai)

    for j in range(0, i):
        if(h[i] == a[j]):
            number += 1
        if(a[i] == h[j]):
            number += 1

print(number)
