MOD = 1000000007

def hash(prevHash, trans, token):
    v = prevHash
    for i in range(len(trans)):
        v = (v * 31 + ord(trans[i])) % MOD
    return (v * 7 + token) % MOD

