n = int(input())
string = input()

if(n < 26):
    print('NO')
else:
    lowered = string.lower()
    list_string = [c for c in lowered]
    string_set = set(list_string)

    if(len(string_set) == 26):
        print("YES")
    else:
        print('NO')
