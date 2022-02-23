from sys import stdin

def pg():
    ans = [2]
    for a in range(3,1500):
        for b in ans:
            if a%b==0:
                break
        else:
            ans.append(a)
    return ans

def main():
    input = stdin.readline

    primes = pg()

    Q = int(input())
    for a in stdin.readlines():
        c = 0
        num = int(a)
        i = 0
        for n in range(1,int(num**0.5)+1):
            if num%n==0:
                c += 1
                if n**2 != num:
                    while primes[i] < n:
                        i += 1
                    print(primes[i])
                    if n < primes[i]:
                        c += 1
        print(c)



if __name__ == "__main__":
    main()