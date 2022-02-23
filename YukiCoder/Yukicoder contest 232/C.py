N = int(input())
req = [0 for i in range(N)]
c = 0
for a in range(1,N+1):
    print("?",N-1)
    print(" ".join(map(str, [i for i in range(1,N+1) if i != a])))
    res = int(input())
    if res == 0:
        req[a-1] = 1
        c += 1
print("!",c)
print(" ".join(map(str, [i+1 for i in range(N) if req[i] == 1])))

# print(req)