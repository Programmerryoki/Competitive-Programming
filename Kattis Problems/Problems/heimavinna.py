line = input().split(";")
pages = set()
for L in line:
    if "-" in L:
        s,e = [int(i) for i in L.split("-")]
        for j in range(s,e+1):
            pages.add(j)
    else:
        pages.add(int(L))
print(len(pages))