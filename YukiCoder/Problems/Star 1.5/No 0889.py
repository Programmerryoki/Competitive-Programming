N = int(input())
if N <= 1:
    print(N)
    exit()
for i in range(2,int(N**0.5)+1):
    if N%i == 0:
        break
else:
    print("Sosu!")
    exit()
if 2 < N and (N**0.5).is_integer() and round(N**0.5)**2 == N:
    print("Heihosu!")
    exit()
if 2 < N and (N**(1/3)).is_integer() and round(N**(1/3))**3 == N:
    print("Ripposu!")
    exit()
s = 0
for n in range(1,N):
    if N%n == 0:
        s += n
if N == s:
    print("Kanzensu!")
    exit()
print(N)