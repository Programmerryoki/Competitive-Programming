N = int(input())
c = set()
for i in range(1,int(N**0.5)+1):
    if N%i == 0:
        c.add(str(i) + str(N//i))
        c.add(str(N//i) + str(i))
print(len(c))