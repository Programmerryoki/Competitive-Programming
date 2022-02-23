def maximum(l):
    ma = 0
    total = 0
    """c = 0
    for a in range(len(l)):
        total += l[a]
        c += 1
        if float(total) / c > ma:
            ma = float(total) / c
    return ma"""
    for i, a in enumerate(l, 1):
        total += a
        if float(total) / i > ma:
            ma = float(total) / i
    return ma


n = int(input())
lst = [int(i) for i in input().split()]
print(max(maximum(lst), maximum(lst[::-1])))