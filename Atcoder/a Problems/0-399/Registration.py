S = input()
T = input()
if S == T[:-1] and len(S) == len(T) - 1:
    print("Yes")
else:
    print("No")