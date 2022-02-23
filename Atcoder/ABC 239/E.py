from sys import setrecursionlimit
setrecursionlimit(10**6)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.cleft = 0
        self.cright = 0
        self.count = 1

class BSTS:
    def __init__(self):
        self.root = None
        self.vals = []
        self.avals = []

    def add(self, val):
        self.avals.append(val)
        if not self.root:
            self.root = Node(val)
            return
        tmp = self.root
        while True:
            if tmp.val == val:
                tmp.count += 1
                break
            if tmp.val < val:
                tmp.cright += 1
                if tmp.right:
                    tmp = tmp.right
                else:
                    tmp.right = Node(val)
                    break
            else:
                tmp.cleft += 1
                if tmp.left:
                    tmp = tmp.left
                else:
                    tmp.left = Node(val)
                    break

    def getKlar(self, K):
        tmp = self.root
        while True:
            # print(K, tmp.val, end="")
            tc = tmp.count
            if tmp.cright >= K:
                # print(" r")
                tmp = tmp.right
            elif tmp.cright < K <= tmp.cright + tc:
                # print()
                return tmp.val
            else:
                # print(" l")
                K -= tmp.cright + tc
                tmp = tmp.left

    def print(self):
        self._dfs(self.root)
        print(self.vals)

    def _dfs(self, node):
        if node.left:
            self._dfs(node.left)
        self.vals.append((node.val, node.count, node.cleft, node.cright))
        if node.right:
            self._dfs(node.right)

# bt = BSTS()
# arr = [1,3,5,2,4,6,1,5,3]
# for i in arr:
#     bt.add(i)
# bt.print()
# for i in range(len(arr)):
#     print(i+1,bt.getKlar(i+1))

N,Q = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]
graph = {i:set() for i in range(1, N+1)}
for _ in range(N-1):
    A,B = [int(i) for i in input().split()]
    graph[A].add(B)
    graph[B].add(A)
Qs = {}
QQ = [[int(i) for i in input().split()] for _ in range(Q)]
for i in range(Q):
    V,K = QQ[i]
    if V not in Qs:
        Qs[V] = {}
    Qs[V][K] = -1
# print(Qs)

seen = {1}
def dfs(cur):
    global Qs, seen
    leaf = True
    bt = None
    for nxt in graph[cur]:
        if nxt not in seen:
            leaf = False
            seen.add(nxt)
            tmp = dfs(nxt)
            # print(cur, tmp)
            if bt:
                for v in tmp.avals:
                    bt.add(v)
            else:
                bt = tmp
    if leaf:
        bt = BSTS()
    bt.add(X[cur-1])
    if cur in Qs:
        for k in Qs[cur]:
            Qs[cur][k] = bt.getKlar(k)
        # print(cur)
        # bt.print()
    return bt

dfs(1)
ans = [0]*Q
for i,[v,k] in enumerate(QQ):
    ans[i] = Qs[v][k]
print("\n".join(str(i) for i in ans))