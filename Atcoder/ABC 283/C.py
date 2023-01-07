S = input()
tp = 0
i = 0
while i < len(S):
    if i < len(S)-1 and S[i] == "0" and S[i+1] == "0":
        i += 1
    tp += 1
    i += 1
print(tp)