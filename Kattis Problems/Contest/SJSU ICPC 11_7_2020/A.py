import re
from sys import setrecursionlimit
setrecursionlimit(10**8)

r,c = map(int, input().split())
row = []
for _ in range(r):
    k, *rest = [int(i) for i in input().split()]
    row.append(rest)
col = []
for _ in range(c):
    k, *rest = [int(i) for i in input().split()]
    col.append(rest)

rop = []
for rp in row:
    pos = []
    for i in range(2**r):
        n = bin(i)[2:]; n = "0"*(r - len(n)) + n
        # print(re.sub(r"0+", " ", n), re.sub(r"0+", " ", n).split())
        pt = [len(i) for i in re.sub(r"0+", " ", n).split()]
        # print(pt,rp)
        if pt == rp:
            pos.append(n)
    rop.append(pos)

count = []
def recur(i,choice):
    global count
    if i == len(rop):
        if choice in count:
            return
        for i in range(c):
            pat = "".join([j[i] for j in choice])
            pt = [len(i) for i in re.sub(r"0+", " ", pat).split()]
            if pt != col[i]:
                return
        count.append(choice)
    for j in rop[i]:
        recur(i+1,choice + [j])

recur(0,[])
# for i in count:
#     for j in i:
#         print(j)
#     print()
print(len(count))