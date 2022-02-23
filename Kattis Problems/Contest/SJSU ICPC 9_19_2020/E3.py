from sys import stdin
from bisect import bisect_left

class node:
    def __init__(self, val):
        self.val = val
        self.num = 1
        self.left = None
        self.right = None
        self.child = 0

    def print(self):
        print("\"",self.val,"\"", self.num, self.child)
        if self.left:
            print(self.val,"l", end=": ")
            self.left.print()
        if self.right:
            print(self.val,"r", end=": ")
            self.right.print()

def main():
    input = stdin.readline

    n = int(input())
    root = None
    ts = 0
    for _ in range(n):
        a = int(input())
        path = []
        if root:
            temp = root
            while temp:
                if temp.val == a:
                    temp.num += 1
                    path.append(0)
                    break
                elif temp.val < a:
                    if temp.right:
                        temp.child += 1
                        temp = temp.right
                        path.append(1)
                    else:
                        path.append(1)
                        temp.right = node(a)
                        break
                else:
                    if temp.left:
                        temp.child += 1
                        temp = temp.left
                        path.append(-1)
                    else:
                        path.append(-1)
                        temp.left = node(a)
                        break
        else:
            root = node(a)

        t = 0
        temp = root
        for i in path:
            if i == 0:
                if temp.right:
                    t += temp.right.child + temp.right.num
            elif i == -1:
                if temp.right:
                    t += temp.right.child + temp.right.num
                t += temp.num
                temp = temp.left
            else:
                temp = temp.right
                if not temp:
                    break
        # if a != root.val:
        #     t += root.num
        ts += t
        # print(path, t)
    print(ts)
    # root.print()


if __name__ == "__main__":
    main()