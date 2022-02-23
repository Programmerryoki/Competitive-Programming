class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

head = tmp = Node(0)
N = int(input())
S = input()
for i in range(1,N+1):
    node = Node(i)
    if S[i-1] == "L":
        if tmp.prev:
            tmp.prev.next, node.prev = node, tmp.prev
        else:
            head = node
        node.next, tmp.prev = tmp, node
    else:
        if tmp.next:
            tmp.next.prev, node.next = node, tmp.next
        node.prev, tmp.next = tmp, node
    tmp = node
ans = []
while head:
    ans.append(head.val)
    head = head.next
print(" ".join(str(i) for i in ans))