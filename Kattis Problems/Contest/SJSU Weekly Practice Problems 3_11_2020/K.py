class Node:
    def __init__(self, val):
        self.val = val
        self.nextNode = []
        self.nextval = []

    def addNext(self, val):
        self.nextNode.append(val)
        self.nextval.append(val.val)

tree = Node("-1")
t = int(input())
for _ in range(t):
    n = int(input())
    for _ in range(n):
        line = input()
        head = tree
        for a in line:
            if a in head.nextval:
                head = head.nextNode[head.nextval.index(a)]
            else:
                head.nextNode