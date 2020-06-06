string = input()
lower_count, upper_count = 0, 0

for char in string:
    if(char.islower()):
        lower_count += 1
    else:
        upper_count += 1

if(upper_count > lower_count):
    print(string.upper())
else:
    print(string.lower())
