from collections import Counter, defaultdict
line = ""
while True:
    try:
        line += input()
    except:
        break
S = defaultdict(int, Counter(line.lower()))
for a in range(ord("a"), ord("z")+1):
    print(chr(a),":",S[chr(a)])