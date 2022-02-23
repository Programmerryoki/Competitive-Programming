P, N = [int(i) for i in input().split()]
parts = []
for a in range(N):
    part = input()
    if part not in parts:
        parts.append(part)
        if len(parts) == P:
            print(a + 1)
            break
if len(parts) < P:
    print("paradox avoided")