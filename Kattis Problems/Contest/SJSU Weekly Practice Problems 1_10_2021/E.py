

numbers = [["xxxxx","x...x","x...x","x...x","x...x","x...x","xxxxx"],
           ["....x","....x","....x","....x","....x","....x","....x"],
           ["xxxxx","....x","....x","xxxxx","x....","x....","xxxxx"],
           ["xxxxx","....x","....x","xxxxx","....x","....x","xxxxx"],
           ["x...x","x...x","x...x","xxxxx","....x","....x","....x"],
           ["xxxxx","x....","x....","xxxxx","....x","....x","xxxxx"],
           ["xxxxx","x....","x....","xxxxx","x...x","x...x","xxxxx"],
           ["xxxxx","....x","....x","....x","....x","....x","....x"],
           ["xxxxx","x...x","x...x","xxxxx","x...x","x...x","xxxxx"],
           ["xxxxx","x...x","x...x","xxxxx","....x","....x","xxxxx"]]
plus = [".....","..x..","..x..","xxxxx","..x..","..x..","....."]

inp = [input() for i in range(7)]
for i in range(7):
    lst = []
    string = inp[i]
    while string:
        lst.append(string[:5])
        string = string[6:]
    inp[i] = lst

num1 = ""
k = 0
while True:
    n = [j[k] for j in inp]
    k += 1
    try:
        num1 += str(numbers.index(n))
    except:
        break
num2 = ""
for i in range(k,len(inp[0])):
    n = [j[i] for j in inp]
    i += 1
    try:
        num2 += str(numbers.index(n))
    except:
        break
# print(num1, num2)
ans = int(num1) + int(num2)
al = ["" for i in range(7)]
for dig in str(ans):
    num = numbers[int(dig)]
    for i in range(7):
        al[i] += num[i] + "."
print("\n".join(i[:-1] for i in al))