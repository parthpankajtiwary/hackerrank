N = input()
K = input()

candies = []
for x in range(N):
	candies.append(int(raw_input()))
candies.sort()
best = candies[-1]

for x in xrange(N-K+1):
    if(candies[x+K-1] - candies[x]) < best:
        best = candies[x+K-1] - candies[x]
print best  