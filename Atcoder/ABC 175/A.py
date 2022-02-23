S = input()
print(3 if len(set(S))==1 and S[0]=="R" else 2 if (S[0]==S[1] or S[1]==S[2]) and S[1]=="R" else 1 if "R" in S else 0)