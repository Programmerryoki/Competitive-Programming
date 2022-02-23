inputs = []
while True:
    line = input()
    if not line:
        break
    inputs.append([int(i) for i in input().split()])

inputs.sort(key=lambda x: x[1])
