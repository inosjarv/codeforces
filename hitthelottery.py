n = int(input())
count = 0
if(n/100):
    count += int(n/100)
    n -= int(n/100)*100

if(n/20):
    count += int(n/20)
    n -= int(n/20)*20

if(n/10):
    count += int(n/10)
    n -= int(n/10)*10

if(n/5):
    count += int(n/5)
    n -= int(n/5)*5

count += n


print(count)
