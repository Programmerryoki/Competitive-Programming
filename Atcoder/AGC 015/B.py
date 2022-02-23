total = 0
S = input()
for i in range(len(S)):
    if S[i] == "U":
        total += len(S)-i-1
        total += i * 2
    else:
        total += (len(S)-i-1) * 2
        total += i
print(total)