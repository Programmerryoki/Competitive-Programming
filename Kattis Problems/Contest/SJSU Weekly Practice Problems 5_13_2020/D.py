n = int(input())
line = input().split()
s = [[int(j),i] for i,j in enumerate(line,1)]
s.sort(reverse=True)
if s[0][0] <= sum([i[0] for i in s]) - s[0][0]:
    print(" ".join(map(str, [i[1] for i in s])))
else:
    print("impossible")