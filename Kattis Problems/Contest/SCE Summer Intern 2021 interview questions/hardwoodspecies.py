from sys import stdin

def main():
    total = 0
    trees = {}
    for tree in stdin.readlines():
        tree = tree.strip()
        if tree in trees:
            trees[tree] += 1
        else:
            trees[tree] = 1
        total += 1

    trees = list(trees.items())
    trees.sort(key=lambda x: x[0])
    print("\n".join(i[0]+" "+str(i[1] * 100 / total) for i in trees))

if __name__ == "__main__":
    main()