inputstring = input()

count, flag = 1, False

for i in range(len(inputstring)-1):
    nextidx = i+1
    if(inputstring[i]==inputstring[nextidx]):
        count+=1
        if(count>=7):
            flag=True
            break
    else:
        count=1
if(flag):
    print("YES")
else:
    print("NO")
