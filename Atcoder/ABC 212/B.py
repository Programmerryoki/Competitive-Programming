pw = input()
if len(set(pw)) == 1:
    print("Weak")
    exit()
count = 0
for i in range(3):
    if (int(pw[i]) + 1) % 10 == int(pw[i+1]):
        count += 1
print("Strong" if count < 3 else "Weak")