t = int(input())
for _ in range(t):
    n = int(input())
    if (n//2)%2 == 1:
        print("NO")
        continue

    even = [i*2 for i in range(1,n//2+1)]
    odd = [i*2-1 for i in range(1,n//2)]
    # print(even, odd)
    odd += [((2+n)*n)//4 - sum(odd)]
    print("YES")
    print(" ".join(map(str, even + odd)))