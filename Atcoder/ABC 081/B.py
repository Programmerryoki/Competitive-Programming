N = int(input())
A = [int(i) for i in input().split()]
print(min([min(bin(i)[::-1].index("1"), len(bin(i))-2) for i in A]))