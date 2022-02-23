N = int(input())
rank = {i:set() for i in range(1,N+1)}
P = [0]*N
for i in range(N):
    p = int(input())
    rank[i+1].add(p)
    P[i] = p

done = [0]*N
Q = int(input())
ans = [""]*Q
for q in range(Q):
    # print(rank)
    # print(done)
    a,b = [int(i) for i in input().split()]
    if not b in rank[a]:
        stack = [a]
        while True:
            if -1 in rank[stack[-1]]:
                break
            if done[stack[-1]-1]:
                break
            p = rank[stack[-1]].pop()
            rank[stack[-1]].add(p)
            stack.append(p)
        for i in range(len(stack)-1, 0, -1):
            rank[stack[i-1]].update(rank[stack[i]])
            done[stack[i]-1] = 1
    ans[q] = "Yes" if b in rank[a] else "No"
print("\n".join(ans))