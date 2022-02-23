N = int(input())
first = input()
seen = {first}
for _ in range(N-1):
    w = input()
    if w[0] != first[-1]:
        print("No")
        break
    if w in seen:
        print("No")
        break
    seen.add(w)
    first = w
else:
    print("Yes")