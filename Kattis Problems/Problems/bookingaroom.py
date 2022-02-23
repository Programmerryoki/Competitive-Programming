r,n = [int(i) for i in input().split()]
rooms = [int(input()) for i in range(n)]
for i in range(1, r+1):
    if i not in rooms:
        print(i)
        break
else:
    print("too late")