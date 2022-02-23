man = lambda x: sum([abs(i) for i in x])
yuku = lambda x: (sum([i**2 for i in x]))**0.5
chebu = lambda x: max([abs(i) for i in x])

N = int(input())
x = [int(i) for i in input().split()]
print(man(x))
print(yuku(x))
print(chebu(x))