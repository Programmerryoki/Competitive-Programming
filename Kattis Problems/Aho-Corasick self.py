class DicTree:
    def __init__(self, id):
        self.state = id
        self.failure = 0
        self.parent = None
        self.child = []
        self.value = ""

    def createTree(self, terms):
        for w in terms:
            for c in w:
                if c not in self.child:
                    self.child.append(DicTree(len(self.child)))

    def setValue(self, val):
        self.value = val

    def print(self):
        return self.value

Aho = DicTree(0)
Aho.setValue("a")
print(Aho.print())