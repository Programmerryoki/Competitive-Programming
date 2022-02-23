mapping = [set(),set("abc"),set("def"),set("ghi"),set("jkl"),set("mno"),set("pqrs"),set("tuv"),set("wxyz")]

def getmap(w):
    for i,s in enumerate(mapping):
        if w in s:
            return str(i+1)

N = int(input())
dic = {}
for _ in range(N):
    word = input()
    temp = dic
    for i,w in enumerate(word):
        pt = temp
        n = getmap(w)
        try:
            temp = temp[n][1]
        except:
            temp[n] = [0, {}]
            temp = temp[n][1]
        if i == len(word)-1:
            pt[n][0] += 1
# print(dic)
S = input()
temp = dic
for w in S:
    pt = temp
    try:
        temp = temp[w][1]
    except:
        print(0)
        exit()
print(pt[S[-1]][0])