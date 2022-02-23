L,R = [int(i)-1 for i in input().split()]
S = input()
print(S[:L]+S[L:R+1][::-1]+S[R+1:])