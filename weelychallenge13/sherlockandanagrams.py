
t = input()
answers = []
for x in xrange(t):
    s = raw_input()
    pairs = []
    count = 0
    strings = [s[i:j] for i in xrange(len(s)) for j in xrange(i+1, len(s)+1) if s[i:j] != s]
    strings.sort(key=len)
    print strings
    for s in strings:
        search = [x for x in strings if len(x) == len(s)]
        search.pop(search.index(s))
        print search
        for x in search:
            if sorted(x) == sorted(s) and ((x, s) not in pairs and (s, x) not in pairs):
                if x == s:
                    pairs.append((x, s))
                else:
                    pairs.append((s, x))
                    pairs.append((x, s))
                count += 1
    print count
