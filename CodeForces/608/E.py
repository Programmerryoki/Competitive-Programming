# n, k = map(int, input().split())
# i = 1
# while i <= n:
#

n, k = map(int, input().split())
t = [0 for i in range(n)]
for a in range(1,n+1):
    num = a
    ans = []
    while num != 1:
        t[num-1] += 1
        ans.append(num)
        if num%2 == 0:
            num //= 2
        else:
            num -= 1
    else:
        t[0] += 1
        ans.append(1)
    # print(a,ans)
    print(" ".join(map(str, t)))