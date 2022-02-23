def dfs(current, stack, seen, ngraph):
    stack.append(current)
    seen.add(current)
    for node in ngraph[current]:
        if not node in seen:
            dfs(node, stack, seen, ngraph)

def main():
    N = int(input())
    characters = {}
    knows = {}
    speaks = {}
    for _ in range(N):
        name, lang, *understand = input().split()
        characters[name] = [lang, understand]
        if lang in speaks:
            speaks[lang].add(name)
        else:
            speaks[lang] = {name}
        for l in understand + [lang]:
            if l in knows:
                knows[l].add(name)
            else:
                knows[l] = {name}
    print(knows)
    print(speaks)
    ngraph = {i:set() for i in characters}
    rgraph = {i:set() for i in characters}
    for name, [lang, und] in characters.items():
        for ppl in knows[lang]:
            if ppl != name:
                ngraph[name].add(ppl)
                rgraph[ppl].add(name)
        for u in und:
            if not u in speaks:
                continue
            for n in speaks[u]:
                if n != name:
                    ngraph[n].add(name)
                    rgraph[name].add(n)
    print(ngraph)
    print(rgraph)
    SCC = []
    stack = []
    seen = set()
    for i in characters:
        if not i in seen:
            dfs(i, stack, seen, ngraph)
    tpo = {i:N - j for j,i in enumerate(stack)}
    print(tpo)
    seen = set()
    for i in stack:
        if not i in seen:
            stac = []
            dfs(i, stac, seen, rgraph)
            SCC.append(stac)

    print(SCC)
    print(max(SCC, key=len))
    print(len(characters) - len(max(SCC, key=len)))

if __name__ == "__main__":
    main()