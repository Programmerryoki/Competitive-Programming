from sys import stdin

def main():
    input = stdin.readline

    count = {}
    total = 0
    for line in stdin.readlines():
        treename = line[:-1]
        if not treename in count:
            count.setdefault(treename, 0)
        count[treename] += 100
        total += 1

    lst = [i[0]+" "+str(i[1]/total) for i in count.items()]
    lst.sort()
    print("\n".join(lst))

if __name__ == "__main__":
    main()