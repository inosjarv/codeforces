n = int(input())
seq = []
no_of_people_on_train = 0
for i in range(n):
    row = input().split()
    for i in range(2):
        row[i] = int(row[i])
    seq.append(row)

capacity = 0
for i in range(n):
    no_of_entries, no_of_exits = seq[i][1], seq[i][0]
    no_of_people_on_train += (no_of_entries - no_of_exits)
    capacity = max(no_of_people_on_train, capacity)


print(capacity)
