class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def appendleft(self, val):
        node = Node(val)
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def append(self, val):
        node = Node(val)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def pop(self, value):
        if value > self.length:
            return "ERROR"
        self.length -= 1
        if value == 1:
            remove = self.tail
            if remove == self.head and remove == self.tail:
                self.head = None
                self.tail = None
                return remove.val
            if remove == self.head:
                self.head = self.tail
                self.tail.prev = None
                return remove.val
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return remove.val
        else:
            if value == 2:
                remove = self.tail.prev
            else:
                remove = self.tail.prev.prev
            if remove == self.head:
                if value == 2:
                    self.head = self.tail
                    self.tail.prev = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
                return remove.val
            remove.prev.next = remove.next
            remove.next.prev = remove.prev
            return remove.val

    def popleft(self, value):
        if value > self.length:
            return "ERROR"
        self.length -= 1
        if value == 1:
            remove = self.head
            if remove == self.head and remove == self.tail:
                self.head = None
                self.tail = None
                return remove.val
            if remove == self.tail:
                self.tail = self.head
                self.head.next = None
                return remove.val
            self.head.next.prev = None
            self.head = self.head.next
            return remove.val
        else:
            if value == 2:
                remove = self.head.next
            else:
                remove = self.head.next.next
            if remove == self.tail:
                if value == 2:
                    self.tail = self.head
                    self.head.next = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
                return remove.val
            remove.prev.next = remove.next
            remove.next.prev = remove.prev
            return remove.val

    def print(self):
        s = []
        order = []
        node = self.head
        while node:
            order.append(node.val)
            next = str(node.next.val) if node.next else "None"
            prev = str(node.prev.val) if node.prev else "None"
            s.append(prev+"<-"+str(node.val)+"->"+next)
            node = node.next
        print(" ".join(map(str, order)))
        print(" ".join(s))


N = int(input())
S = input()
A = LinkedList()
outputs = []
for i in range(len(S)):
    val = i+1
    if S[i] == "L":
        A.appendleft(val)
    elif S[i] == "R":
        A.append(val)
    elif S[i] == "A":
        outputs.append(A.popleft(1))
    elif S[i] == "B":
        outputs.append(A.popleft(2))
    elif S[i] == "C":
        outputs.append(A.popleft(3))
    elif S[i] == "D":
        outputs.append(A.pop(1))
    elif S[i] == "E":
        outputs.append(A.pop(2))
    elif S[i] == "F":
        outputs.append(A.pop(3))

    # print(S[i])
    # A.print()
    # print(outputs)
if outputs:
    print("\n".join(map(str, outputs)))