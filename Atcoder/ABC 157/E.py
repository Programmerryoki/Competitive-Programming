N = int(input())
S = list(input())
Q = int(input())
ans = [set(S[:i+1]) for i in range(len(S))]
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        S[int(query[1])-1] = query[2]
        ans = [set(S[:i+1]) for i in range(len(S))]
    else:
        print(len(set(S[int(query[1])-1:int(query[2])])))