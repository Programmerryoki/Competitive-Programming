P1 = input().split()
P2 = input().split()
if int(P1[1]) < int(P2[1]):
    print(P2[0])
elif int(P1[1]) > int(P2[1]):
    print(P1[0])
else:
    print(-1)