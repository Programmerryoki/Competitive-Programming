case = 0
while True:
    try:
        n = int(input())
        case += 1
    except:
        break
    print("Case "+str(case)+":")
    s = [int(input()) for i in range(n)]
    sums = list(set([i+j for i in s for j in s if i != j]))
    sums.sort()
    m = int(input())
    # print(sums)
    for a in range(m):
        q = int(input())
        i = 0
        while i < len(sums) - 1 and abs(sums[i] - q) > abs(sums[i+1] - q):
            i += 1
        print("Closest sum to",q,"is "+str(sums[i])+".")