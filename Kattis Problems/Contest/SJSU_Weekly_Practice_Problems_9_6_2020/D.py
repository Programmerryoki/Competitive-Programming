ans = []
while True:
    n = int(input())
    if n == 0:
        break
    l1 = [int(input()) for i in range(n)]
    l2 = [int(input()) for i in range(n)]
    dic = dict(zip(sorted(l1),sorted(l2)))
    ans.append("\n".join(map(str, [dic[i] for i in l1])))
print("\n\n".join(ans))