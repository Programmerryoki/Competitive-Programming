N = int(input())
magic = ""
while N > 0:
    if N&1:
        N -= 1
        magic += "A"
    else:
        N //= 2
        magic += "B"
print(magic[::-1])