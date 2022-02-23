class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def printing(node):
    while node:
        print(node.prev.val if node.prev else node.prev, end=" ")
        print(node.val, end=" ")
        print(node.next.val if node.next else node.next)
        node = node.next
    print()

T = int(input())
for _ in range(T):
    m,r = map(int, input().split())
    a = [int(i) for i in input().split()]
    temp = Node(1)
    ll = [temp, None]
    for i in range(2,m+1):
        temp.next = Node(i)
        temp.next.prev = temp
        temp = temp.next
    ll[-1] = temp
    # printing(ll[0])
    ans = []
    for i in a:
        temp = ll[0]
        ns = 0
        # print(i,ll[0].val, ll[1].val)
        while temp:
            if temp.val == i:
                if temp == ll[0] and temp == ll[1]:
                    pass
                elif temp == ll[1]:
                    ll[1] = temp.prev
                    temp.prev.next, temp.prev = None, None
                    temp.next = ll[0]
                    ll[0].prev = temp
                    ll[0] = temp
                elif temp != ll[0]:
                    temp.prev.next, temp.prev = temp.next, None
                    temp.next = ll[0]
                    ll[0].prev = temp
                    ll[0] = temp
                break
            temp = temp.next
            ns += 1
            # print(i,ll[0].val, ll[1].val)
            # printing(ll[0])
        ans.append(ns)
        # printing(ll[0])
    print(*ans)