n = int(input())
x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]

m = 0
merged_list = list()

for i in range(1, x[0]+1):
    merged_list.append(x[i])
for i in range(1, y[0]+1):
    merged_list.append(y[i])

# print(merged_list)d

for i in range(1, n+1):
    if i not in merged_list:
        m = 1
        print("Oh, my keyboard!")
        break
if m == 0:
    print("I become the guy.")
