primes = [2]
for i in range(3, 10**5):
    for p in primes:
        if i%p==0:
            break
    else:
        primes.append(i)

printing = []
for i in primes:
    if "0" in set(str(i)):
        continue
    printing.append(str(len(str(i)))+"\n"+str(i))
print(len(printing))
print("\n".join(printing))