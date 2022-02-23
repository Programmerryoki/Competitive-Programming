# tmp = 0
# for i in range(151):
#     tmp ^= i
#     print(i, tmp)
#

t = int(input())
for _ in range(t):
    a,b = [int(i) for i in input().split()]
    xor = 0 if (a-1)%4==3 or a-1 == 0 else a-1 if (a-1)%4==0 else 1 if (a-1)%4==1 else a
    if xor == b:
        print(a)
    elif xor^b == a:
        print(a + 2)
    else:
        print(a + 1)