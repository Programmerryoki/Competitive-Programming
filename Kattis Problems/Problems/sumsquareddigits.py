digits = "0123456789ABCDEF"

def SSD(b, n):
    return sum(map(lambda x: int(digits.index(x))**2, list(str(n))))


def number(b, n):
    total = ""
    p = 1
    while n > 0:
        mod = n % b
        n //= b
        total = str(digits[mod]) + total
    return total


n = int(input())
for a in range(n):
    line = input().split(" ")
    b = int(line[1])
    n = int(line[2])
    num = number(b, n)
    print(a+1, SSD(b,num))
