letter = " abcdefghijklmnopqrstuvwxyz"
l, w = [int(i) for i in input().split()]
if l <= w <= l*26:
    if w % l == 0:
        print(letter[w//l] * l)
    else:
        n = w // (l-1)
        r = w - n*(l-1)
        while n > 26:
            n -= 1
            r += n
        if r != 0:
            print(letter[n]*(l-1) + letter[r])
        else:
            print(letter[n]*(l-2) + letter[n-1] + letter[1])
else:
    print("impossible")


# letter = " abcdefghijklmnopqrstuvwxyz"
# l, w = [int(i) for i in input().split()]
# if l <= w <= l*26:
#     if l > 2:
#         if w % l == 0:
#             print(letter[w//l] * l)
#         n = w // (l-1)
#         r = w - n*(l-1)
#         if r != 0:
#             print(letter[n]*(l-1) + letter[r])
#         else:
#             print(letter[n]*(l-2) + letter[n-1] + letter[1])
#     elif l == 2:
#         if w%2==0:
#             print(letter[w//2]*2)
#         else:
#             print(letter[w//2 + 1] + letter[w//2])
#     else:
#         print(letter[w])
# else:
#     print("impossible")