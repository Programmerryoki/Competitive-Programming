clas = ["upper", "middle", "lower"]
T = int(input())
for _ in range(T):
    n = int(input())
    ppl = []
    longest = 0
    for _ in range(n):
        line = input().split()
        ppl.append([line[1].split("-"), line[0][:-1]])
        longest = max(longest, len(ppl[-1][0]))
    ppl.sort(key=lambda x: [[clas.index(i) for i in x[0][::-1]] + [1]*(longest - len(x[0])), x[1]])
    print("\n".join([i[1] for i in ppl]))
    print("="*30)