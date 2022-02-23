n, m = [int(i) for i in input().split()]
rule = {chr(i):chr(i) for i in range(ord("A"), ord("Z"))}
for i in range(n):
    line = input().split()
    rule[line[0]] = line[2]
S = input()
for i in range(m):
    t = ""
    for s in S:
        t += rule[s]
    S = t
print(S)