set1 = input()

list1 = set1[1:-1]

if not list1:
    print(0)
else:
    print(len(set(list1.split(', '))))
