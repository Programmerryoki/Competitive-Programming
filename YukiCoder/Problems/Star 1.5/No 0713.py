N = int(input())
t = 0
for n in range(2,N+1):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            break
    else:
        t += n
print(t)