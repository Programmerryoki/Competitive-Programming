S,T = input().split()
A,B = map(int, input().split())
U = input()
if S == U:
    A -= 1
elif T == U:
    B -= 1
print(A,B)