n = int(input())
count=0
for _ in range(n):
    
    seq=[int(x) for x in input().split()]

    if(sum(seq)>=2):
        count+=1
    
print(count)    