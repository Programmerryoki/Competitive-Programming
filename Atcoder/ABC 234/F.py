S = input()
CS = [0]*26
for s in S:
    CS[ord(s)-ord("a")] += 1
checked = set()
def dfs(index, used):
    global checked
    tu = tuple(used)
    if tu in checked:
        return
    checked.add(tu)
    for i in range(26):
        if used[i] < CS[i]:
            used[i] += 1
            dfs(index, used)
            used[i] -= 1

dfs(0, [0]*26)
print(len(checked))