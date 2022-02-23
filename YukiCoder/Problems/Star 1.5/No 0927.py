x = [i for i in input()]
y = "".join(sorted(x,reverse=True))
print(y[:-2]+y[-1]+y[-2])