S = [int(i) for i in input().split()]
S.remove(max(S))
S.remove(min(S))
print("{:.2f}".format(sum(S)/4))