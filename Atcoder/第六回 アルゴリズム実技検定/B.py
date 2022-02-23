S = input()
for index in range(1, len(S), 4):
    if S[index] == "o":
        print(index//4 + 1)
        exit()
print("none")