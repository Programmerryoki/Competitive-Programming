from copy import deepcopy

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    dic = {}
    for i in range(n):
        print(dic)
        pname = input()
        m, *ingrid = input().split()
        singrid = set(ingrid)
        j, *engrid = input().split()
        sengrid = set(engrid)
        for grid in ingrid:
            if grid in dic:
                dic[grid] = dic[grid] & sengrid
            else:
                dic[grid] = deepcopy(sengrid)
        for key in dic.keys():
            if key not in singrid:
                dic[key] = dic[grid] - sengrid
    at = []
    for i in dic.keys():
        for j in dic[i]:
            at.append([i,j])
    ans.append(at)
print("\n".join("\n".join("("+i[0]+", "+i[1]+")" for i in j) for j in ans))