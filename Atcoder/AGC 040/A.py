S = input()
arr = [0]*(len(S) + 1)
cn = 0
for i in range(len(S)):
    if S[i] == "<":
        cn += 1
    else:
        cn = 0
    arr[i+1] = cn
cn = 0
for i in range(len(S)-1, -1, -1):
    if S[i] == ">":
        cn += 1
    else:
        cn = 0
    arr[i] = max(arr[i], cn)
# print(arr)
print(sum(arr))