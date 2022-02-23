primes = [2]
for num in range(3,int((10**7)**0.5)+1):
    for p in primes:
        if num%p==0:
            break
    else:
        primes.append(num)

class Node:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.parent = None
        self.left = None
        self.right = None
        self.factor = {val}
        mn = int(val**0.5)
        for p in primes:
            if p <= mn:
                if val%p==0:
                    self.factor.add(p)
                    self.factor.add(val//p)

def walk(tmp, d):
    if tmp.left:
        # print(tmp.val, tmp.left.val)
        walk(tmp.left,tmp.val)
    print(str(d)+":"+str(tmp.val), end=" ")
    if tmp.right:
        # print(tmp.val, tmp.right.val)
        walk(tmp.right,tmp.val)

n = int(input())
a = [int(i) for i in input().split()]
root = current = Node(0, 0)
nodes = [root]+[None]*n
for i,num in enumerate(a):
    # print(num)
    node = Node(num, i+1)
    nodes[i+1] = node
    current.right, node.parent = node, current
    temp = node
    current = node
    while True:
        temp = temp.parent
        if temp == root:
            break
        if not len(temp.factor & node.factor):
            continue
        if temp.right == node:
            print("impossible")
            exit()
        if not temp.right.left:
            tp = temp.parent
            tr = temp.right
            tp.right, temp.parent, tr.parent, tr.left, temp.right = tr, tr, tp, temp, None
        elif temp.right.left:
            tp = temp.parent
            tr = temp.right
            trl = tr.left
            tp.right, trl.parent, tr.left, trl.right, tr.parent = trl, tp, None, tr, trl
            temp.right = None
            if trl.left:
                tmp = trl.left
                while tmp.left:
                    tmp = tmp.left
                temp.parent, tmp.left = tmp, temp
            else:
                trl.left, temp.parent = temp, trl
            temp = trl
    # walk(root.right, 0)
    # print()

# walk(root.right, 0)
# print()

print(" ".join(map(str, [i.parent.index for i in nodes[1:]])))
