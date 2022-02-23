def main():
    N,K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    if K == 1:
        print(sum(A))
        exit()
    ks = [0] * K
    A.sort(reverse=True)
    odd = False
    i = 0
    j = 0
    while j < N:
        if odd:
            if i == 0:
                if ks[i] < ks[i+1]:
                    ks[i] += A[j]
                    j += 1
                odd = not odd
            else:
                ks[i] += A[j]
                j += 1
                if ks[i] >= ks[i-1]:
                    i -= 1
        else:
            if i == K - 1:
                if ks[i] < ks[i-1]:
                    ks[i] += A[j]
                    j += 1
                odd = not odd
            else:
                ks[i] += A[j]
                j += 1
                if ks[i] >= ks[i+1]:
                    i += 1
    print(min(ks))

if __name__ == '__main__':
    main()