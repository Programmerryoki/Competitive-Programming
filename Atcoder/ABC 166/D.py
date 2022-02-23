ans = set()
i = 0
while i**5 <= 10**10:
    ans.add(i**5)
    ans.add(-i**5)
    i += 1

X = int(input())
for i in ans:
    if X - i in ans:
        print(int(i**0.2), -int((X-i)**0.2))
        break