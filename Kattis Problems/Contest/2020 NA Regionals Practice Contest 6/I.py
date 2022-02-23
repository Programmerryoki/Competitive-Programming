n = int(input())
fnames = input().split()
files = {}
for _ in range(n):
    fn, k = input().split(); k = int(k)
    imports = []
    for i in range(k):
        line = input()[7:].split(", ")
        imports += line
    files[fn] = set(imports)
# print(files)

seen = {fnames[0]}
order = {(fnames[0],)}
que = [fnames[0]]
ml = float("inf")
mlst = []
while order:
    lst = order.pop()
    seen = set(lst)
    node = lst[-1]
    # print("\n",lst)
    for n in files[node]:
        if n in seen:
            index = lst.index(n)
            if index - len(order) < ml:
                ml = index - len(order)
                mlst = lst[index:]
        else:
            seen.add(n)
            order.add(lst + (n,))
    # print(order)
print("SHIP IT" if ml == float("inf") else " ".join(mlst))
# print(ml, mlst)