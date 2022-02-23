from functools import reduce

product = lambda nums: reduce(lambda x,y: x*y, nums)

n = int(input())
dutch = input().split()
m = int(input())
correct = {i:set() for i in set(dutch)}
incorrect = {i:set() for i in set(dutch)}
for _ in range(m):
    d,e,c = input().split()
    if c == "correct":
        if d in correct:
            correct[d].add(e)
        else:
            correct[d] = {e}
    if d in incorrect:
        incorrect[d].add(e)
    else:
        incorrect[d] = {e}

nums = [len(correct[i]) for i in dutch]
pd = product(nums)
if pd == 1:
    print(" ".join([list(correct[i])[0] for i in dutch]))
    print("correct")
    exit()
elif pd == 0:
    if product([len(incorrect[i]) for i in dutch]) == 1:
        print(" ".join([list(incorrect[i])[0] for i in dutch]))
        print("incorrect")
        exit()
wrong = [len(incorrect[i]) for i in dutch]
pdw = product(wrong) - pd
print(pd, "correct")
print(pdw, "incorrect")