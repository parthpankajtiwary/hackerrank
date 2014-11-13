

def search(a,b):
    seen = {}
    seen[a] = True
    q = []

    for x in adj[a]:
        if x != b:
            seen[x] = True
            q.append(x)
    s = len(q) + 1
    while q:
        n = q.pop()
        for x in adj[n]:
            if x not in seen:
                seen[x] = True
                q.append(x)
                s += 1
    return (s+1)%2

[N,M] = [int(x) for x in raw_input().split(' ')]
edges = []
adj = {}
for a in xrange(1,N+1):
    adj[a] = []

for a in xrange(M):
    [x,y] = [int(z) for z in raw_input().split(' ')]
    adj[x].append(y)
    adj[y].append(x)
    edges.append((x,y))

count = 0
for e in edges:
    (x,y) = e
    if search(x,y):
        count += 1
        adj[x].remove(y)
        adj[y].remove(x)

print count
