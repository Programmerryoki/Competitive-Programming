class MachineAC:
    class State:
        def __init__ (self, id):
            self.id   = id
            self.next = {}

        def has_key(self, x):
            for a in self.next.keys():
                if x == a:
                    return True
            return False
            #return self.next.values(x)

    def __init__ (self, terms):
        self.state  = [ MachineAC.State(0) ]
        self.output = [[]]
        self._make_goto(terms)
        self._make_failure()

    def _make_goto(self, terms):
        for term in terms:
            cur = self.state[0]
            for x in term:
                if not cur.has_key(x):
                    new = MachineAC.State( len(self.state) )
                    cur.next[x] = new
                    self.state.append(new)
                    self.output.append([])
                cur = cur.next[x]
            s = cur.id
            self.output[s].append(term)

    def _make_failure(self):
        failure = [0] * len(self.state)
        queue   = [ 0 ]
        while len(queue) > 0:
            s = queue.pop(0)
            for x in self.state[s].next.keys():
                next = self.g(s, x)
                if next is not None:
                    queue.append(next)
                if s != 0:
                    f = failure[s]
                    while self.g(f, x) is None:
                        f = failure[f]
                    failure[next] = self.g(f, x)
                    self.output[next].extend( self.output[failure[next]] )
        self.failure = failure

    def g(self, s, x):
        if x in self.state[s].next:
            return self.state[s].next[x].id
        else:
            if s == 0:
                return 0
            else:
                return

    def match (self, query):
        # print(self.output)
        ans = [[] for i in range(len(noVowelLine))]
        s = 0
        for i in range(len(query)):
            while self.g(s, query[i]) is None:
                s = self.failure[s]
            s = self.g(s, query[i])
            for x in self.output[s]:
                # print ('%d,%d => %s' % (i - len(x) + 1, i, x))
                ans[i-1].append(x)
        return ans

# ac = MachineAC(['ab', 'bc', 'bab', 'd', 'abcde'])

# print ('in: xbabcdex')
# ac.match('xbabcdex')
#
# print ('in: abc')
# ac.match('abc')

def noVowel(s):
    vowels = "aeiouAEIOU"
    ans = ""
    for a in s:
        if a not in vowels:
            ans += a
    return ans


f = open("nvwlstest1.txt", "r")

fline = f.readline()
n = int(fline)
dic = []
ma = 0
for a in range(n):
    line = (f.readline())[:-1]
    noV = noVowel(line)
    dic.append(noV)
noVowelLine = f.readline()
f.close()

# print(dic)

ac = MachineAC(dic)
print("in:")
output = ac.match("x"+noVowelLine)
print(output)

