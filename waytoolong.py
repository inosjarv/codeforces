n = int(input())

for _ in range(n):
    inputstr = input()
    result=""
    if(len(inputstr) <= 10):
        print(inputstr)
    
    else:
        result+=inputstr[0]
        temp = len(inputstr[1:len(inputstr)-1])
        result+= str(temp) + inputstr[-1]
        print(result)