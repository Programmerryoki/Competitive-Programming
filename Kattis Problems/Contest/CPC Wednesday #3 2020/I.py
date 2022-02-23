def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for a in range(3,int(n**0.5)+1,2):
        if n%a==0:
            return False
    return True

p,a = [int(i) for i in input().split()]
while p != 0 and a != 0:
    if isprime(p):
        print("no")
        p,a = [int(i) for i in input().split()]
        continue
    pattern = [a]
    n = 0
    m = 0
    num = a
    while n <= p:
        num = num*a%p
        n += 1
        if num in pattern:
            break
        pattern.append(num)
    if pattern[p%len(pattern)-1] == a:
        print("yes")
    else:
        print("no")

    p,a = [int(i) for i in input().split()]