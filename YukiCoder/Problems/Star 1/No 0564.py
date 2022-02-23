H,N = [int(i) for i in input().split()]
h = [int(input()) for i in range(N-1)] + [H]
h.sort(reverse=True)
index = str(h.index(H)+1)
if index[-1] == "1":
    print(index + "st")
elif index[-1] == "2":
    print(index + "nd")
elif index[-1] == "3":
    print(index + "rd")
else:
    print(index + "th")