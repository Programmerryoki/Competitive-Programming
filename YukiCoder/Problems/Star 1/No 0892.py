n = [int(i) for i in input().split()]
s = sum([n[i] for i in range(len(n)) if i%2==0])
print(":-)") if s%2==0 else print(":-(")