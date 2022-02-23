h0 = int(input())
d = h0//8
c = h0%8
if c == 0:
    print(d*8)
elif c <= 5:
    print(d*8+5)
else:
    print((d+1)*8)
#
# h = int(input())
# ans = []
# for i in range(1,h):
#     c = int(1.5*i**2 + 0.5*i)
#     if c%4 == 0:
#         ans.append(i)
#     if len(ans) == 20:
#         print(" ".join(map(str, ans)))
#         ans = []
# print(" ".join(map(str, ans)))