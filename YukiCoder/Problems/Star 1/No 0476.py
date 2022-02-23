n,a = [int(i) for i in input().split()]
print("YES" if n*a == sum([int(i) for i in input().split()]) else "NO")