s = input().split()
stack = []
for a in range(len(s)):
    w = s[a]
    if w == "+":
        stack.append(stack.pop(-2)+stack.pop())
    elif w == "-":
        stack.append(stack.pop(-2)-stack.pop())
    elif w == "*":
        stack.append(stack.pop(-2)*stack.pop())
    else:
        stack.append(int(w))
print(stack[0])