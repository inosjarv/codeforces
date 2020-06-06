m = "hello"
x = 0
flag = False
string = input()
for s in string:
    if s == m[x]:
        x += 1
        if(x == 5):
            flag = True
            break
if(flag):
    print("YES")
else:
    print("NO")
