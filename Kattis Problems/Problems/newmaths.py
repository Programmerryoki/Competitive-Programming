mn = 10001
dig = [[0,0] for i in range(len(str(mn))*2-1)]
for n in range(mn):
    sn = str(n)
    ans = [0]*(len(sn)*2 - 1)
    for i in range(len(sn)):
        for j in range(len(sn)):
            ans[j+i] = (ans[j+i] + int(sn[i])*int(sn[j])) % 10
    print(n,"".join(map(str, ans)))
    for i in range(len(sn)*2-2, -1, -1):
        dig[len(sn)*2-2-i][int(ans[i])&1] += 1
ml = len(str(max([i[0] for i in dig] + [i[1] for i in dig])))
print("\n".join(" ".join(["{:>{}}".format(str(i[j]), ml) for i in dig[::-1]]) for j in range(2)))
print(dig)

# N = input()
# if not len(N)&1 or sum([(int(N[i])&1)^(1-len(N)&1) for i in range(1,len(N),2)]):
#     print(-1)
#     exit()
# ln = (len(N)+1) // 2