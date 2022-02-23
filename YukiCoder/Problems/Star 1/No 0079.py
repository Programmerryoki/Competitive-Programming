from collections import Counter
N = int(input())
LC = Counter([int(i) for i in input().split()]).most_common()
print(max(LC, key = lambda x: (x[1], x[0]))[0])