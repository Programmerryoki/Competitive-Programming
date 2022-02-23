N = int(input())
city = [[int(i) for i in input().split()] + [j] for j in range(N)]
# k = [[i[0], i[1]] for i in city]
city.sort()
ans = [0]*N
for x,y,j in city:
    for i in range(N):
        if city[i][1] <= y and city[i][0] <= x:
            ans[j] += 1
        elif city[i][1] >= y and city[i][0] >= x:
            ans[j] += 1
print("\n".join(map(str, ans)))