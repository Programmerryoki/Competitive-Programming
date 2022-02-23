T = int(input())
for _ in range(T):
    n = int(input())
    dic = {}
    for _ in range(n):
        name,attr = input().split()
        if attr in dic:
            dic[attr] += 1
        else:
            dic[attr] = 1
    total = 1
    for key in dic:
        total *= dic[key]+1
    print(total - 1)