N = int(input())
num = [1]*(N+1)
num[0] = 0
for a in range(3,len(num),3):
    num[a] = 0
for b in range(5,len(num),5):
    num[b] = 0
t = 0
for a in range(len(num)):
    if num[a] == 1:
        t += a
print(t)