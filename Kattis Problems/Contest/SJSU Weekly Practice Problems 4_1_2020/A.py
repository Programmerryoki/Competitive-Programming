n = int(input())
for _ in range(n):
    stack = []
    adv = input()
    for a in adv:
        if a in "$|*":
            stack.append(a)
        elif a in "btj":
            if len(stack) == 0:
                print("NO")
                break
            if a == "b":
                if stack.pop() != "$":
                    print("NO")
                    break
            elif a == "t":
                if stack.pop() != "|":
                    print("NO")
                    break
            elif a == "j":
                if stack.pop() != "*":
                    print("NO")
                    break
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")