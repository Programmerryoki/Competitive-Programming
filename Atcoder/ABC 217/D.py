from sys import stdin

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_height = 0
        self.right_height = 0

    def angle(self):
        return self.right_height - self.left_height

    def max_depth(self):
        return max(self.right_height, self.left_height)

class BinarySearchTree:
    def __init__(self, L):
        self.L = L
        self.root = None

    def insert(self, x):
        if not self.root:
            self.root = Node(x)
            return
        self._insert(self.root, x, None)

    def _insert(self, node, x, parent):
        if node.val < x and node.right:
            node.right_height = self._insert(node.right, x, node)
        elif node.val > x and node.left:
            node.left_height = self._insert(node.left, x, node)
        else:
            if node.val < x:
                node.right = Node(x)
            else:
                node.left = Node(x)
            return 0
        if node.angle() < -1:
            if node.left and node.left.angle() >= 1:
                self.rotate_left(node.left.right, node.left, node)
            self.rotate_right(node.left, node, parent)
        elif node.angle() > 1:
            if node.right and node.right.angle() <= -1:
                self.rotate_right(node.right.left, node.right, node)
            self.rotate_left(node.right, node, parent)
        else:
            return node.max_depth()

    def rotate_left(self, pivot, node, parent):
        node.right, node.right_height = pivot.left, pivot.left_height
        pivot.left, pivot.left_height = node, node.max_depth()
        if parent:
            parent.right, parent.right_height = pivot, pivot.max_depth()

    def rotate_right(self, pivot, node, parent):
        node.left, node.left_height = pivot.right, pivot.right_height
        pivot.right, pivot.left_height = node, node.max_depth()
        if parent:
            parent.left, parent.right_height = pivot, pivot.max_depth()

    def find_length(self, x):
        bound = [0, self.L]
        tmp = self.root
        while tmp:
            if tmp.val < x:
                bound[0] = max(bound[0], tmp.val)
                tmp = tmp.right
            elif tmp.val > x:
                bound[1] = min(bound[1], tmp.val)
                tmp = tmp.left
        return bound[1] - bound[0]

    def print(self):
        tmp = []
        self.inorder(self.root, tmp)
        print(tmp)

    def inorder(self, node, vals):
        if node is not None:
            self.inorder(node.left, vals)
            vals.append(node.val)
            self.inorder(node.right, vals)

def main():
    input = stdin.readline
    L,Q = [int(i) for i in input().split()]
    cuts = BinarySearchTree(L)
    ans = []
    for _ in range(Q):
        c,x = [int(i) for i in input().split()]
        # print(c,x)
        if c == 1:
            cuts.insert(x)
        else:
            ans.append(str(cuts.find_length(x)))
        # cuts.print()
    print("\n".join(ans))


if __name__ == '__main__':
    main()