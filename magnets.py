n = int(input())
magnets = list()
count = 0
for _ in range(n):
    magnet = input()
    magnets.append(magnet)

for i in range(1, len(magnets)):
    if(magnets[i-1] != magnets[i]):
        count += 1
print(count + 1)
