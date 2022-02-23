from collections import Counter
line = input()
N = len(line)
cline = Counter(line)
if len(cline) == 1:
    print(-1)
    exit()
lline = [list(i) for i in cline.most_common()]
if lline[0][1] > N//2:
    lline.append([lline[0][0], lline[0][1] - N//2])
    lline[0][1] = N//2
print("".join([i[0]*i[1] for i in lline]))