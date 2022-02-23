class Node:
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.next = {}
        self.end = 0

N = int(input())
start = Node("Start")
for _ in range(N):
    word = input()
    head = start
    for i,w in enumerate(word):
        try:
            head = head.next[w]
        except:
            head.next[w] = Node(w)
            head = head.next[w]
        if i != len(word) - 1:
            head.count += 1
        else:
            print(head.count)
            head.count += 1
            head.end += 1