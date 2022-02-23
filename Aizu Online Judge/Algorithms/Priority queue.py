import sys, heapq
def main():
    input = sys.stdin.readline
    que = []
    ans = []
    while True:
        a = input()
        if a[0] == "i":
            heapq.heappush(que, -int(a[7:]))
        elif a[2] == "t":
            ans.append(-heapq.heappop(que))
        else:
            break
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()

# import sys, heapq
# def main():
#     input = sys.stdin.readline
#     que = []
#     ans = []
#     while True:
#         a = input()
#         if a[0] == "i":
#             heapq.heappush(que, -int(a[7:]))
#         elif a[2] == "t":
#             ans.append(-heapq.heappop(que))
#         else:
#             break
#     print("\n".join(map(str, ans)))
#
#
# if __name__ == "__main__":
#     main()

# import sys, heapq
# def main():
#     input = sys.stdin.readline
#     que = []
#     ans = []
#     while True:
#         a = input()
#         try:
#             i = a.index(" ")
#             n = int(a[i+1:])
#             heapq.heappush(que, -n)
#         except:
#             if len(a) != 4:
#                 m = heapq.heappop(que)
#                 ans.append(-m)
#             else:
#                 break
#     print("\n".join(map(str, ans)))
#
#
# if __name__ == "__main__":
#     main()

# import sys
# def main():
#     input = sys.stdin.readline
#
#     counter = {}
#
#     class Node:
#         def __init__(self,n):
#             self.val = n
#             self.next = None
#
#         # def getVal(self):
#         #     return self.val
#         #
#         # def setNext(self, ob):
#         #     self.next = ob
#         #
#         # def getNext(self):
#         #     return self.next
#
#
#     class LinkedList:
#         def __init__(self):
#             self.head = None
#             self.tail = None
#
#         def add(self, ob : Node):
#             if self.head == None:
#                 self.head = ob
#                 self.tail = ob
#             elif ob.val >= self.head.val:
#                 self.head, ob.next = ob, self.head
#             else:
#                 node = self.head
#                 while node.next:
#                     if ob.val <= node.next.val:
#                         node = node.next
#                     else:
#                         break
#                 if node == self.tail:
#                     node.next, self.tail = ob, ob
#                 else:
#                     node.next, ob.next = ob, node.next
#             counter[ob.val] = 1
#
#         def extract(self) -> Node:
#             ob = self.head.val
#             if counter[ob] == 1:
#                 self.head = self.head.next
#                 del counter[ob]
#             else:
#                 counter[ob] -= 1
#             return ob
#
#         def print(self):
#             node = self.head
#             vals = []
#             while node:
#                 vals.append(node.val)
#                 node = node.next
#             print(counter)
#             print(" -> ".join(map(str, vals)))
#
#
#
#
#     que = LinkedList()
#     ans = []
#     while True:
#         a = input()
#         try:
#             i = a.index(" ")
#             n = int(a[i+1:])
#             if n not in counter:
#                 que.add(Node(n))
#             else:
#                 counter[n] += 1
#             # que.print()
#         except:
#             if len(a) != 4:
#                 m = que.extract()
#                 # que.print()
#                 ans.append(m)
#             else:
#                 break
#     print("\n".join(map(str, ans)))
#
# if __name__ == "__main__":
#     main()