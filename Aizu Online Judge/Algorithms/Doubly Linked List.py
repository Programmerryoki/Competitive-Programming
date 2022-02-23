import sys


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            node.next = temp
            temp.prev = node
            self.head = node

    def delete(self, n):
        if self.head == self.tail and self.head.val == n:
            self.head = None
            self.tail = None
        elif n == self.head.val:
            self.deleteF()
        elif n == self.tail.val:
            self.deleteL()
        else:
            temp = self.head
            while temp:
                if temp.val == n:
                    temp.prev.next, temp.next.prev = temp.next, temp.prev
                    break
                temp = temp.next

    def deleteF(self):
        temp = self.head
        temp.prev = None
        self.head = temp.next

    def deleteL(self):
        temp = self.tail.prev
        temp.next = None
        self.tail = temp

    def print(self):
        ans = []
        node = self.head
        while node:
            # print(node.val, [node.prev.val if node.prev else None, node.next.val if node.next else None])
            ans.append(node.val)
            node = node.next
        print(" ".join(map(str, ans)))


class Node:
    def __init__(self, n):
        self.val = n
        self.next = None
        self.prev = None


input = sys.stdin.readline
ll = LinkedList()
n = int(input())
for a in range(n):
    s = input()
    if s[0] == "i":
        ll.add(Node(int(s[7:])))
    elif s[6] == " ":
        # print(int(s[6:]))
        ll.delete(int(s[7:]))
    elif s[6] == "F":
        ll.deleteF()
    elif s[6] == "L":
        ll.deleteL()
    # ll.print()
ll.print()