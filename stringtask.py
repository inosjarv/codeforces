inputstr = input()
resultstr  = ""
vowels = "AEIOUYaeiouy"
for s in inputstr:
    if((vowels.__contains__(s)) == False):
        resultstr+= "." + s.lower()

    
    
print(resultstr)
        