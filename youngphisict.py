n = int(input())
seq = []
for i in range(n):
    row = input().split()
    for j in range(len(row)):
        row[j] = int(row[j])
    seq.append(row)

flag = False
j = 0
sumx, sumy, sumz = 0, 0, 0
for i in range(n):
    sumx += seq[i][0]
    sumy += seq[i][1]
    sumz += seq[i][2]

if(sumx == 0 and sumy == 0 and sumz ==0):
    print("YES")
else:
    print("NO")
