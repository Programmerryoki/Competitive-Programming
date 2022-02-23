Y,M,D = [int(i) for i in input().split()]
if 1989 <= Y <= 2019:
    if Y != 1989 and Y != 2019:
        print("Yes")
    elif Y == 1989 and 1 <= M:
        if M != 1:
            print("Yes")
        elif 8 <= D:
            print("Yes")
        else:
            print("No")
    elif Y == 2019 and M <= 4:
        print("Yes")
    else:
        print("No")
else:
    print("No")