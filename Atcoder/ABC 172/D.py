N = int(input())
total = 0
for i in range(1,N+1):
    total += ((i  + (N - N%i)) * (N//i))//2
print(total)