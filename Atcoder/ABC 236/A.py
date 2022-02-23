S = input()
a,b = [int(i)-1 for i in input().split()]
print(S[:a]+S[b]+S[a+1:b]+S[a]+S[b+1:])