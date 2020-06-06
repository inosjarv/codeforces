n = int(input())
hate = "I hate"
that = "that"
love = "I love"
it = "it"
space = " "
result = ""
i = 1
if n == 1:
    result = hate + space + it
if n > 1:
    while(i <= n):
        if(i % 2 == 1):
            result += hate + space

        if(i % 2 == 0):
            result += love + space

        if(i == n):
            result += space + it

        if(i != n):
            result += that + space
        i += 1
print(result)
