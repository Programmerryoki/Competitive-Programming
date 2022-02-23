from collections import Counter

N = int(input())
cs = Counter([input() for i in range(N)])
print(cs.most_common(1)[0][0])