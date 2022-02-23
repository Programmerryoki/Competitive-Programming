n = int(input())
print(int("".join(list(bin(n)[2:][::-1])), 2))