from itertools import combinations_with_replacement
import re

qa,_,qb,_,qc = input().split()
rep = "."
nq = qa.count("?")+qb.count("?")
rc = qc.replace("?", rep)
count = 0
for nl in combinations_with_replacement([i for i in range(10)], nq):
    i = 0
    aa = ""
    for j in qa:
        if j == "?":
            aa += str(nl[i])
            i += 1
        else:
            aa += j
    if aa[0] == "0" and len(aa) != 1:
        continue
    bb = ""
    for j in qb:
        if j == "?":
            bb += str(nl[i])
            i += 1
        else:
            bb += j
    if bb[0] == "0" and len(bb) != 1:
        continue
    print(aa,bb)
    cc = str(int(aa)^int(bb))
    if re.fullmatch(rc, cc):
        print("\t",aa,bb,cc)
        count += 1
print(count)

# 13 10 7
# 13 11 6
# 13 12 1
# 13 13 0
# 13 14 3
# 13 15 2
# 23 16 7
# 23 17 6
# 23 18 5
# 23 19 4

# import re
#
# qa,_,qb,_,qc = input().split()
# rep = "."
# ra = qa.replace("?", rep); rb = qb.replace("?", rep); rc = qc.replace("?", rep)
# count = 0
# for a in range(10**(len(qa)-1),10**9):
#     na = str(a)
#     if len(na) > len(ra):
#         break
#     if not re.fullmatch(ra, na):
#         continue
#     for b in range(10**(len(qb)-1),10**9):
#         nb = str(b)
#         if len(nb) > len(rb):
#             break
#         if not re.fullmatch(rb, nb):
#             continue
#         nc = str(a^b)
#         if re.fullmatch(rc, nc):
#             print(a,b,nc)
#             count += 1
# print(count)

# import re
#
# qa,_,qb,_,qc = input().split()
# rep = "."
# # nq = qa.count("?")+qb.count("?")+qc.count("?")
# ra = qa.replace("?", rep); rb = qb.replace("?", rep); rc = qc.replace("?", rep)
# count = 0
# for a in range(1,10**9):
#     na = str(a)
#     if len(na) > len(ra):
#         break
#     if not re.fullmatch(ra, na):
#         continue
#     for b in range(1,10**9):
#         nb = str(b)
#         if len(nb) > len(rb):
#             break
#         if not re.fullmatch(rb, nb):
#             continue
#         for c in range(1,10**9):
#             nc = str(c)
#             if max(len(bin(a)), len(bin(b))) < len(bin(c)):
#                 break
#             if not re.fullmatch(rc, nc):
#                 continue
#             if a ^ b == c:
#                 print(a,b,c)
#                 print(bin(a))
#                 print(bin(b))
#                 print(bin(c))
#                 count += 1
# print(count)