from itertools import permutations
c = int(input())
for _ in range(c):
    pos = set()
    s = input()

    def permu(rn,nu):
        if rn in pos:
            return
        if rn != "":
            pos.add(int(rn))
        for i,n in enumerate(nu):
            permu(rn+n, nu[:i]+nu[i+1:])
    permu("",list(s))
    count = 0
    for i in pos:
        n = int(i)
        if n <= 1:
            continue
        for j in range(2,int(n**0.5)+1):
            if n%j == 0:
                break
        else:
            count += 1
    print(count)