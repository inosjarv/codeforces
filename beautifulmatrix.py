seq = []
for i in range(5):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    seq.append(row)

steps = 0
for i in range(5):
    for j in range(5):
        if(seq[i][j]==1):
            steps=abs(2-i) + abs(2-j)
print(steps)
