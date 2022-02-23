n = int(input())
x = [int(i) for i in input().split()]

def recur(n):
    if n == len(x)-1:
        return [x[n], 1]
    ans = recur(n+1)
    # print(x[n], ans)
    return [ans[0]*x[n]+ans[1], ans[0]]

ans = recur(0)
print(str(ans[0])+"/"+str(ans[1]))