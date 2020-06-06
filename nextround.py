n, k = map(int, input().split())
seq=[int(x) for x in input().split()]

count=0
for i in range(len(seq)):

    if(seq[i]==0 or seq[i]<seq[k-1]):
        break
    if(seq[i]>= seq[k-1]):
        count+=1
    
print(count)