i = int(input())
for _ in range(i):
    N = int(input())
    if N%10==0 and N%8==0:
        print("ikisugi")
    elif N%10==0:
        print("sugi")
    elif N%8==0:
        print("iki")
    else:
        print(N//3)