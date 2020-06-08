string1 = input()
string2 = input()

string3 = input()

string3 = sorted(string3)
combined_String = sorted(string1+string2)

if(string3 == combined_String):
    print('YES')
else:
    print('NO')
