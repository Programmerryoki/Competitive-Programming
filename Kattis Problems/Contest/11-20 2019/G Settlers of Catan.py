class Node:
    def __init__(self, id):
        self.id = id
        self.child = []

    def getId(self):
        return self.id

    def setNode(self, pos, node):
        self.node()