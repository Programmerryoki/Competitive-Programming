N = int(input())
for case in range(N):
    M, V = [int(i) for i in input().split()]
    nodes = []
    for a in range((M-1)//2):
        nodes.append([int(i) for i in input()])
    for a in range((M+1)//2):
        nodes.append([int(input())])

    count = 0
    gate = ["0111","0001"]
    def search(tp, rv):
        node = nodes[tp]
        if len(node) == 1:
            return node[0]

        if rv == -1:
            nl = search(tp*2, -1)
            nr = search(tp*2+1, -1)
            if nl or nr:
                return 1
            else:
                return 0
        else:
            