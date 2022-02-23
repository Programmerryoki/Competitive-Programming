K = int(input())
n = bin(K)[2:]
if n.count("1")==1:
    print(2**(len(n)-1), 0)
else:
    print(2**len(n), len(n)-n[::-1].index("1"))