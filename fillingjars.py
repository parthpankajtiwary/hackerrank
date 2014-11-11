N, M = map(int, raw_input().split())

sum = 0
for x in xrange(M):
    a, b, candies = map(int, raw_input().split())
    sum += ((b-a) + 1)*candies
print sum/N  