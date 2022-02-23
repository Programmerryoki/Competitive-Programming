N = int(input())
for i in range(N-100, N+101):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        continue
    print(i)
    break