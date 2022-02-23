S = input()
words = []
c = 0
i = 0
while i < len(S):
    if S[i].isupper():
        if c:
            words.append(S[:i+1])
            S = S[i+1:]
            c = 0
            i = -1
        else:
            c = 1
    i += 1
words.sort(key=lambda x: x.lower())
print("".join(words))