def to_vocab(n):
    if n == 0: return "a"
    ret = ""
    while n > 0:
        ret += chr(ord("a")+n%26)
        n //= 26
    return ret

A,B = [int(i) for i in input().split()]
ans = [to_vocab(i) for i in range(-(-B//2))] * 2
print(" ".join(ans[:max(-(-B//2), A)]))