#Creating syllables dictionary type
S = int(input())
sylla = [set() for i in range(26)]
for _ in range(S):
    s = input()
    sylla[ord(s[0]) - ord("a")].add(s)
# print(sylla)

# Decomposing
def match(s, d):
    # print(s)
    ans = set()
    pos = sylla[ord(s[0]) - ord("a")]
    for a in pos:
        if a == s[:len(a)]:
            if len(s) - len(a) == 0:
                ans.add(d + 1)
                break
            temp = match(s[len(a):], d+1)
            ans = ans | temp
    return ans


haiku = [input().split() for i in range(3)]
sn = [[] for i in range(3)]
for i in range(3):
    for j,w in enumerate(haiku[i]):
        temp = match(w, 0)
        sn[i].append(temp)
# for a in range(len(sn)):
#     print(haiku[a])
#     print(a, sn[a])

# Fine
def combi(arr, s, i, t):
    # print(s, i, t)
    if i == len(arr) and s == t:
        return True
    elif i == len(arr):
        return False

    for a in arr[i]:
        if s + a <= t:
            if combi(arr, s+a, i+1, t):
                return True
    return False

p = True
if combi(sn[0], 0, 0, 5):
    if combi(sn[1], 0, 0, 7):
        if combi(sn[2], 0, 0, 5):
            print("haiku")
            p = False
if p:
    print("come back next year")