while True:
    n = int(input())
    if n == 0:
        break

    fooddic = {}
    for _ in range(n):
        person, *foods = input().split()
        for food in foods:
            if food in fooddic:
                fooddic[food].append(person)
            else:
                fooddic[food] = [person]
    ans = list(fooddic.items())
    ans.sort()
    for i,lst in ans:
        print(i," ".join(sorted(lst)))
    print()