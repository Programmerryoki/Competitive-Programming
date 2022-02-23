items = {"b":"$","t":"|","j":"*"}

n = int(input())
for _ in range(n):
    stack = []
    a = input()
    for i in a:
        if i == ".":
            continue
        if i not in items:
            stack.append(i)
        else:
            if not stack or stack[-1] != items[i]:
                print("NO")
                break
            stack.pop()
    else:
        print("YES" if not stack else "NO")