N = int(input())
S = input()
c = 0
for i in range(N):
    for j in range(i+1,N):
        k = j + (j - i)
        if j < k < N:
            b = (S[i], S[j], S[k])
            if "R" in b and "G" in b and "B" in b:
                c += 1
print((N * (N - 1) * (N - 2))//6 - c)
print(c)

# N = int(input())
# S = input()
# R = set()
# B = set()
# G = set()
# for i in range(N):
#     if S[i] == "R":
#         R.add(i)
#     elif S[i] == "B":
#         B.add(i)
#     elif S[i] == "G":
#         G.add(i)
# if len(R) < len(B) and len(B) > len(G):
#     B,G = G,B
# elif len(R) > len(B) and len(R) > len(G):
#     R,G = G,R
#
#
# c = 0
# for r in R:
#     for b in B:
#         p = set()
#         if r < b:
#             p.add(r - (b-r))
#             if ((r + b)/2).is_integer():
#                 p.add((r + b) // 2)
#             p.add(b + (b-r))
#         elif r > b:
#             p.add(b - (r-b))
#             if ((r + b)/2).is_integer():
#                 p.add((r + b) // 2)
#             p.add(r + (r-b))
#
#         c += len(G - p)
# print(c)