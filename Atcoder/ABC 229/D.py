S = input() + " "
oriK = int(input())
xstart = S[0] == "X"
arr = []
j = 1
cur = S[0] == "X"
for i in range(len(S)):
    if (S[i] == "X" and cur) or (S[i] == "." and not cur):
        continue
    if i != 0:
        arr.append(i - j + 1)
        j = i + 1
    cur = not cur
# print(arr)
mv = 0
cv = 0
j = 0
K = oriK
# print(arr)
for i in range(len(arr)):
    if (xstart and not i&1) or (not xstart and i&1):
        cv += arr[i]
        t = [mv, cv]
        if j > 0 and i < len(arr) - 1:
            t.append(cv + min(arr[i+1]+arr[j-1], K))
        if j > 0:
            t.append(cv + min(arr[j-1], K))
        if i < len(arr) - 1:
            t.append(cv + min(arr[i+1], K))
        mv = max(t)
    else:
        if arr[i] <= K:
            K -= arr[i]
            cv += arr[i]
        else:
            while j <= i and K < arr[i]:
                K += arr[j+(1 if xstart else 0)] if oriK >= arr[j] else 0
                cv -= (arr[j] + (arr[j+(1 if xstart else -1)] if xstart or j!=0 else 0))
                j += 2
            if arr[i] <= K:
                K -= arr[i]
                cv += arr[i]
            else:
                K = oriK
                cv = 0
                j = i+1
        t = [mv, cv]
        if j > 0:
            t.append(cv + min(arr[j-1], K))
        mv = max(t)
    # print(i, mv, cv, j, K)
print(mv)