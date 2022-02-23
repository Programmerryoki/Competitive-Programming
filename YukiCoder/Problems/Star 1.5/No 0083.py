N = int(input())
print("7" + "1" * ((N-3)//2) if N&1 else "1"*(N//2))