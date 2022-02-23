N = int(input())
if N == 3 or N == 4 or (N+1)%3==0:
    print("No")
    exit()
elif N > 8:
    ans = [[""]*(N-i) for i in range(1,N)]
    