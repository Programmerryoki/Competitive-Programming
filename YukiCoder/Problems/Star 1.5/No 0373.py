A,B,C,D = [int(i) for i in input().split()]
print((A%D)*(B%D)*(C%D) % D)