N = int(input())
said = set()
prev = ""
for i in range(N):
    word = input()
    if i == 0:
        prev = word
        said.add(word)
        continue
    if word[0] != prev[-1] or word in said:
        print("WIN" if i&1 else "LOSE")
        exit()
    prev = word
    said.add(word)
print("DRAW")