from collections import Counter, defaultdict

integers = [i for i in range(1,51)]
N, K, M = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
cts = []
temp = defaultdict(int)
for i in arr:
    temp[i] += 1
    cts.append(temp.copy())
print(cts)
for _ in range(M):
    line = input()
    if line[0] == "2":
        end = []
        ori = Counter()
        ori = defaultdict(int, ori)
        for i in range(len(arr)):
            ori[arr[i]] += 1
            cts.append(ori)
            n = list(ori.keys())
            n.sort()
            # print(n, ori)
            if n[:K] == integers[:K]:
                end.append(i)
        # print("END")
        # print(end)
        print(cts)
        if len(end) == 0:
            print(-1)
            continue

        mi = end[0] + 1
        for e in end:
            j = 0
            ori = defaultdict(int, Counter(arr[:e+1]))
            # print("ori")
            # print(ori)
            while j <= e:
                ori[arr[j]] -= 1
                if ori[arr[j]] == 0:
                    ori.pop(arr[j])
                n = list(ori.keys())
                # print("l",ori, n)
                n.sort()
                if n[:K] != integers[:K]:
                    if mi > e + 1 - j:
                        mi = e + 1 - j
                    break
                j += 1
            # print(mi, e, j)
        print(mi)
    else:
        line = line.split()
        arr[int(line[1]) - 1] = int(line[2])