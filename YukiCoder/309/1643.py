S = input()
ca = 0
for i in range(len(S)):
    ca += S[i] == "a"
print("a"*(ca+1))