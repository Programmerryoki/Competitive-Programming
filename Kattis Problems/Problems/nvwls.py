vowels = "aeiouAEIOU"


def noVowel(s):
    vowels = "aeiouAEIOU"
    ans = ""
    for a in s:
        if a not in vowels:
            ans += a
    return ans

##################################
f = open("nvwlstest.txt", "r")

fline = f.readline()
n = int(fline)
dic = []
ma = 0
for a in range(n):
    line = (f.readline())[:-1]
    noline = noVowel(line)
    num = (len(line) - len(noline)) / float(len(line))
    dic.append([noline, num, line])
    if num > ma:
        ma = num

noVowelLine = f.readline()

f.close()
# print("finish reading")
# print(n)
# print(dic)
# print(ma)
##################################

"""
n = int(input())
dic = []
ma = 0
for a in range(n):
    line = input()
    noline = noVowel(line)
    num = (len(line) - len(noline)) / float(len(line))
    dic.append([noline, num, line])
    if num > ma:
        ma = num
noVowelLine = input()
"""

dic = sorted(dic, key=lambda x: [x[0], num - x[1]])
# for a in dic:
#     print(a)

nov = [i[0] for i in dic]
# print(nov)

ans = ""
# print(noVowelLine)
a = 0
while a < len(noVowelLine):
    b = 0
    for b in range(len(noVowelLine)):
        if noVowelLine[a:a + b] in nov:
            break
    ans += dic[nov.index(noVowelLine[a:a + b])][2]
    if a + b != len(noVowelLine):
        ans += " "
    a += b
    print(ans)
print(ans)
# print("done")

# 8
# ONE
# MORNING
# SHOT
# AN
# ELEPHANT
# IN
# MY
# PAJAMAS
# NMRNNGSHTNLPHNTNMYPJMS
