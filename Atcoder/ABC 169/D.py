N = int(input())
div = set()
for n in range(1,int(N**0.5)+1):
    if N%n == 0:
        div.add(n)
print(div)