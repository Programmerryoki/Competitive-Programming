name = input().split("-")
print("".join([name[i][0] for i in range(len(name))]))