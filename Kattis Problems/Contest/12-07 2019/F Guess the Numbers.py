from itertools import permutations
s = [int(i) for i in input().split()]
while s[0] != 0 or s[1] != 0:
    nums = s[1:-1]
    result = s[-1]
    comb = permutations(nums,s[0])

    expression = input()
    variable = []
    for a in expression:
        if ord("a") <= ord(a) <= ord("z"):
            variable.append(a)


    for i in comb:
        dic = {}
        for j in range(s[0]):
            dic[variable[j]] = i[j]
        print(expression, i, eval(expression, dic), result)
        if eval(expression, dic) == result:
            print("YES")
            break
    else:
        print("NO")

    s = [int(i) for i in input().split()]