from sys import stdin

class UF:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, pos):
        if pos not in self.parent:
            return None
        if self.parent[pos] == pos:
            return pos
        else:
            self.parent[pos] = self.find(self.parent[pos])
            return self.parent[pos]

    def makeset(self, pos):
        self.parent[pos] = pos
        self.rank[pos] = 0

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx] = rooty
        elif rootx != rooty:
            self.parent[rooty] = rootx
            self.rank[rootx] += 1

def main():
    input = stdin.readline
    H,W = [int(i) for i in input().split()]
    union = UF()
    Q = int(input())
    ans = []
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    for _ in range(Q):
        # print(union)
        t,*rest = [int(i) for i in input().split()]
        if t == 1:
            t = tuple(rest)
            union.makeset(t)
            for dx,dy in moves:
                x,y = t[0]+dx, t[1]+dy
                if 1 <= x <= H and 1 <= y <= W:
                    tmp = (x,y)
                    if union.find(tmp):
                        union.union(t, tmp)
        else:
            a = union.find((rest[0],rest[1]))
            b = union.find((rest[2],rest[3]))
            ans.append("Yes" if a == b and a else "No")
    print("\n".join(ans))

if __name__ == '__main__':
    main()