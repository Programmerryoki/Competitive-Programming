N,M = [int(i) for i in input().split()]
S = input()
T = input()
white = [S.count("A"), T.count("A")]
print(min(white[0], white[1]) + min((len(S) - white[0]), (len(T) - white[1])))