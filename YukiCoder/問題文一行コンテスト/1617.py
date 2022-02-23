S = input()
if len(set(S)) == 1:
    print(-1 if len(S) & 1 else 0)
elif S != S[::-1]:
    print(len(S))
else:
    print(len(S)-2 if len(S) != 3 else -1)