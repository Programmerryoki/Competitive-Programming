num = input().split()
print(max(int("".join(reversed(list(num[0])))), int("".join(reversed(list(num[1]))))))