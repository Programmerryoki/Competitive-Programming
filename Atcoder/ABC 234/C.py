K = int(input())
a = bin(K)[2:]
print("".join("02"[int(i)] for i in a))