tp = 0
while True:
    try:
        line = input()
    except:
        break
    e1, e2 = [[int(j) for j in i.split('-')] for i in line.split(',')]
    if e1[1] < e2[0] or e2[1] < e1[0]:
        continue
    tp += 1
print(tp)

# tp = 0
# while True:
#     try:
#         line = input()
#     except:
#         break
#     e1, e2 = [[int(j) for j in i.split('-')] for i in line.split(',')]
#     if e1[0] <= e2[0] <= e2[1] <= e1[1] or e2[0] <= e1[0] <= e1[1] <= e2[1]:
#         tp += 1
# print(tp)