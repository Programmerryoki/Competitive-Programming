S = input()
print(S[:-2]+S[-2:].upper() if S[-2:] == "ai" else S+"-AI ML Team")