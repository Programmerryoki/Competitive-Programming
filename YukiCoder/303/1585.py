N = int(input())
if N == 1:
    print("Yes")
    exit()
for i in range(round(N**(1/3)), N):
    if i**3 == N:
        print("Yes")
        exit()
    if i**3 > N:
        break
print("No")