import re

patt = "0[xX][0-9A-Fa-f]*"
ans = []
while True:
    try:
        line = input()
    except:
        break

    for num in re.findall(patt, line):
        ans.append(num)
print("\n".join(i + " " + str(int(i, 16)) for i in ans))