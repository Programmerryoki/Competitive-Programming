class Node:
    def __init__(self, val):
        self.val = val
        self.front = None
        self.back = None

N,Q = [int(i) for i in input().split()]
train = {i+1:Node(i+1) for i in range(N)}
ans = []
for _ in range(Q):
    c,*rest = input().split()
    if c == "1":
        x,y = [int(i) for i in rest]
        train[x].back, train[y].front = train[y], train[x]
    elif c == "2":
        x,y = [int(i) for i in rest]
        train[x].back, train[y].front = None, None
    else:
        x = int(rest[0])
        t = train[x]
        while t.front is not None:
            t = t.front
        tmp = []
        while t:
            tmp.append(t.val)
            t = t.back
        ans.append(f"{len(tmp)} "+" ".join(map(str, tmp)))
print("\n".join(ans))