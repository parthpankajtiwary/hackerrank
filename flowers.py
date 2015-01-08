n, k = map(int, raw_input().split())

costArray = [int(x) for x in raw_input().split()]
costArray.sort()
costArray.reverse()
cost = 0
if k < n:
    for x in xrange(k):
        cost += costArray[x]
    for x in xrange(k, n):
        cost += (n-k+1)%n*costArray[x]
else:
    for x in xrange(k):
        cost += costArray[x]
print cost
