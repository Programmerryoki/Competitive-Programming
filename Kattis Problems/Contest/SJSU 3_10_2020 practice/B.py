N = int(input())
name = [input() for i in range(N)]
if name == sorted(name):
    print("INCREASING")
elif name == sorted(name)[::-1]:
    print("DECREASING")
else:
    print("NEITHER")