P = [int(i) for i in input().split()]
print("".join(chr(ord("a")+i-1) for i in P))