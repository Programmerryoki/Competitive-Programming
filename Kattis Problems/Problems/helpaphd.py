n = int(input())
for a in range(n):
    ques = input().split("+")
    if len(ques) == 2:
        print(int(ques[0]) + int(ques[1]))
    else:
        print("skipped")