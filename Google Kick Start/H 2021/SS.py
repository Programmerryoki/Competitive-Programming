class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def isInterest(a, b):
    return (int(b)-int(a)) % 10 == 1

def string(node):
    ans = []
    while node:
        ans.append(node.val)
        node = node.next
    return ans

T = int(input())
for case in range(T):
    N = int(input())
    S = list(input())
    inter = [[] for _ in range(10)]
    head = tmp = Node(S[0])
    for s in S[1:]:
        node = Node(s)
        tmp.next, node.prev = node, tmp
        if isInterest(tmp.val, node.val):
            inter[int(node.val)].append(tmp)
        tmp = node
    tail = tmp
    while sum(len(i) for i in inter) != 0:
        for i, arr in enumerate(inter):
            j = 0
            while j < len(arr):
                node = arr[j]
                j += 1
                # print(i, inter)
                if not node.next or (not node.next and not node.prev):
                    continue
                if isInterest(node.val, node.next.val):
                    node.val = str((int(node.next.val)+1)%10)
                    nnode = node.next
                    nnnode = node.next.next
                    node.next, nnode.prev, nnode.next = nnnode, None, None
                    if nnnode:
                        nnnode.prev = node
                    # print(node.val, nnode.val)
                    # if node.prev:
                    #     print(node.prev.val, node.val, nnode.val)
                    if node.prev and isInterest(node.prev.val, node.val):
                        # print("prev")
                        npv = int(node.prev.val)
                        if npv == i:
                            arr.append(node.prev)
                        else:
                            inter[npv].append(node.prev)
                    elif node.next and isInterest(node.val, node.next.val):
                        # print("cur")
                        nv = int(node.val)
                        if nv == i:
                            arr.append(node)
                        else:
                            inter[nv].append(node)
                # print(i, string(head))
            inter[i].clear()
            # print()
    print(f"Case #{case+1}: {''.join(string(head))}")