def base(j, num):
    nbj = []
    while num > 0:
        nbj.append(num%j)
        num //= j
    for i in range(len(nbj)//2):
        if nbj[i] != nbj[len(nbj)-i-1]:
            return False
    return True

def main():
    a,b,k = [int(i) for i in input().split()]
    count = 0
    for num in range(a,b+1):
        for j in range(2, k+1):
            if not base(j, num):
                break
        else:
            count += 1
    print(count)


if __name__ == '__main__':
    main()