n = list(input())
for a in range(len(n)-3,0,-3):
    n.insert(a,",")
print("".join(n))