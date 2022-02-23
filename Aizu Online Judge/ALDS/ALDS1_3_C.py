# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None
#
# class DLL:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def print(self):
#         temp = self.head
#         val = []
#         while temp != None:
#             val.append(temp.val)
#             # print(temp.prev.val if temp.prev else None, end=" <- ")
#             # print(temp.val, end=" -> ")
#             # print(temp.next.val if temp.next else None)
#             temp = temp.next
#         print(" ".join(val))
#
# n = int(input())
# lst = DLL()
# for _ in range(n):
#     cmd = input()
#     # print(cmd)
#     cs = cmd.split()
#     if len(cs) == 2:
#         if cs[0][0] == "i":
#             node = Node(cs[1])
#             if lst.head:
#                 node.next, lst.head.prev, lst.head = lst.head, node, node
#             else:
#                 lst.head = lst.tail = node
#         else:
#             if lst.head.val == cs[1]:
#                 if lst.head == lst.tail:
#                     lst.head = lst.tail = None
#                     continue
#                 lst.head.prev, lst.head = None, lst.head.next
#                 continue
#
#             temp = lst.head
#             while temp != None:
#                 if temp.val == cs[1]:
#                     if lst.tail == temp:
#                         lst.tail.prev.next, lst.tail = None, lst.tail.prev
#                         break
#                     temp.prev.next, temp.next.prev = temp.next, temp.prev
#                     break
#                 temp = temp.next
#     else:
#         if lst.head == lst.tail:
#             lst.head = lst.tail = None
#             continue
#         if cmd[6] == "F":
#             lst.head.next.prev, lst.head = None, lst.head.next
#         else:
#             lst.tail.prev.next, lst.tail = None, lst.tail.prev
#     # lst.print()
# vals = []
# temp = lst.head
# while temp != None:
#     vals.append(temp.val)
#     temp = temp.next
# print(" ".join(vals))



from collections import deque
from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    lst = deque()
    for _ in range(n):
        cmd = input()
        cs = cmd.split()
        if len(cs) == 2:
            if cs[0][0] == "i":
                lst.appendleft(cs[1])
            else:
                if cs[1] in lst:
                    lst.remove(cs[1])
        else:
            if cmd[6] == "F":
                lst.popleft()
            else:
                lst.pop()
    print(" ".join(map(str, lst)))
if __name__ == "__main__":
    main()