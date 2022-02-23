V = {}
while True:
    try:
        L = input().split()
    except:
        break
    # print(V)
    if L[0] == "define":
        V[L[2]] = int(L[1])
        continue

    try:
        A = V[L[1]]
        B = V[L[3]]
    except:
        print("undefined")
        continue

    EVAL = True
    if L[2] == "=":
        EVAL = A == B
    elif L[2] == ">":
        EVAL = A > B
    else:
        EVAL = A < B
    if EVAL:
        print("true")
    else:
        print("false")


# V = dict()
# while True:
#     try:
#         L = input().split()
#     except:
#         break
#     # print(L)
#     if L[0] == "define":
#         # print(L[2], L[1])
#         V[L[2]] = L[1]
#     else:
#         if L[2] == "=":
#             L[2] += "="
#         try:
#             print(V)
#             print(" ".join(L[1:]))
#             if eval(" ".join(L[1:]), {}, V):
#                 print("true")
#             else:
#                 print("false")
#         except:
#             print("undefined")
#     # print(V)