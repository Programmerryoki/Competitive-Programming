N = int(input())
name = ""
while N > 0:
    name += chr(ord("a") + N%26 - 1) if N%26 != 0 else "z"
    N = (N-1)//26
print(name[::-1])