n, m = map(int, input().split())

for i in range(n):
    if(i % 2 == 0):
        print("#"*m)
    if(i % 4 == 1):
        print("."*(m-1) + "#")
    if(i % 2 == 1 and i % 4 != 1):
        print('#' + "."*(m-1))
