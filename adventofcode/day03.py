import functools
import string

rank = string.ascii_lowercase + string.ascii_uppercase
ts = 0
while True:
    try:
        back = [input() for i in range(3)]
    except:
        break
    ts += rank.index(functools.reduce(lambda x,y: x & y, [set(i) for i in
                                                         back]).pop()) + 1
print(ts)

# import string
#
# rank = string.ascii_lowercase + string.ascii_uppercase
# ts = 0
# while True:
#     try:
#         back = input()
#     except:
#         break
#     c1 = back[:len(back)//2]; c2 = back[len(back)//2:]
#     ts += sum(rank.index(i)+1 for i in set(c1) & set(c2))
# print(ts)