T = int(input())
for _ in range(T):
    input()
    rem = 0
    N = int(input())
    for _ in range(N):
        rem = (int(input()) + rem)%N
    if rem == 0:
        print("YES")
    else:
        print("NO")