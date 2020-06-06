year = int(input())

while(True):
    year += 1
    a, b, c, d = year // 1000, int(year // 100 %
                                   10), int(year // 10 % 10), year % 10

    if(a != b and b != c and c != d and a != c and a != d and b != d):
        break

print(year)
