R, C, ZR, ZC = [int(i) for i in input().split()]
article = []
for a in range(R):
    article.append(input())

for a in range(len(article)):
    txt = ""
    for b in article[a]:
        txt += b*ZC
    article[a] = txt

ans = []
for a in article:
    for b in range(ZR):
        ans.append(a)

for a in ans:
    print(a)