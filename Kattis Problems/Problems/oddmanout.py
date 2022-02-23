N = int(input())
for a in range(N):
    gn = int(input())
    guest = input().split() # [int(i) for i in input().split()]
    for b in guest:
        if guest.count(b) == 1:
            print("Case #" + str(a+1) + ":", b)
            break