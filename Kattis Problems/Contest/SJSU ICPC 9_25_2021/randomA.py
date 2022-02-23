from random import randint

N = 7
case = [randint(1,5000) for i in range(N)]
print(N," ".join(map(str, case)))