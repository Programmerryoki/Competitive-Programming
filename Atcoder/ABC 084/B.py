A,B = [int(i) for i in input().split()]
S = input()
try:
    if len(S) != A + B + 1:
        int("a")
    int(S[:A] + S[A+1:])
    if S[A] != "-":
        int("b")
    print("Yes")
except:
    print("No")