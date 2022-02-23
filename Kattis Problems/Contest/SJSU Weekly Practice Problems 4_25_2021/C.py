from math import ceil

def hash(prevHash, transaction, token):
    MOD = 10**9 + 7
    v = prevHash
    for s in transaction:
        v = (v * 31 + ord(s)) % MOD
    return (v * 7 + token) % MOD

def token_hash(prevHash, transaction):
    MOD = 10**9 + 7
    v = prevHash
    for s in transaction:
        v = (v*31 + ord(s)) % MOD
    # print(v, v * 7)
    tmp = MOD if MOD > v * 7 else MOD * ceil(v * 7 / MOD)
    token = (tmp + 10**7) - (v * 7)
    hashv = (v * 7 + token) % MOD
    return (token, hashv)

def create(prevHash):
    pvs = token_hash(prevHash, transaction)
    # print(pvs)
    print(transaction,pvs[0])
    return pvs

transaction = "charlie-pays-to-eve-9-sg-coins"
create(create(int(input()))[1])
# for i in range(1,141):
#     print(i)
#     num = i*(10**7)
#     pv = create(num)
#     print("hash",hash(num,transaction,pv[0]))
#     num = create(pv[1])
#     print("hash",hash(pv[1],transaction,num[0]))
#     print("-"*50)
# print(hash(140000000,"alice-pays-bob-3-sg-coins",306969470))