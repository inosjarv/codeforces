t = int(input())
users = dict()

for _ in range(t):
    user = input()

    if(user not in users.keys()):
        users[user] = 0
        print("OK")
    else:
        users[user] += 1
        print(user + str(users[user]))
