def concat(l):
    a = 0
    while a < len(l) - 1:
        if l[a] == l[a + 1]:
            del l[a + 1]
        else:
            a += 1
    return l


line = input()
con = concat(list(line))
# con = list(line)

# c = 0
# seen = []
# for a in range(len(con) - 1):
#     try:
#         co = con.index(con[a], a + 1)
#         c += co - a - sum([con[a:co].count(i)-1 for i in con[a:co]])  # con[a:].count(con[a])
#     except:
#         c += len(con) - a - 1
# print(c)

c = 0
seen = []
for a in range(len(con)-1):
    try:
        co = con.index(con[a], a + 1)
        c += co - a
        seen = []
        for b in range(a, co):
            if con[b] not in seen:
                seen.append(con[b])
                c -= (con[b:co].count(con[b])-1)  # con[a:].count(con[a])
    except:
        c += len(con) - a - 1
print(c)

"""
c = 0
for a in range(len(con)-1):
    for b in range(a+1,len(con)):
        # seq = con[a:b+1]
        # if seq.count(con[a]) + seq.count(con[b]) == 2:
        if con[a] not in con[a+1:b+1] and con[b] not in con[a:b]:
            c += 1
print(c)
"""