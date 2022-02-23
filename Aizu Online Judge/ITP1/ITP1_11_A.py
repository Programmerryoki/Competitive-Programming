class Die:
    def __init__(self, labels):
        self.labels = labels
        self.top = 1
        self.d = 0
        self.adj = [[5,3,2,4],[1,3,6,4],[1,5,6,2],[1,2,6,5],[1,4,6,3],[2,3,5,4]]

    def move(self, dire):
        self.d = (self.d + "SWNE".index(dire)) % 4
        nxt = self.adj[self.top-1][self.d]
        self.top, self.d = nxt, self.adj[nxt-1].index(self.top)
        self.d = 2 - self.d if self.d <= 2 else 1

label = [int(i) for i in input().split()]
move = input()
die = Die(label)
for m in move:
    die.move(m)
    print(die.top, die.d)
print(die.labels[die.top-1])