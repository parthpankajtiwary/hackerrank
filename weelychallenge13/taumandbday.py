t = input()


for x in xrange(t):
    b, w = map(int, raw_input().split())
    x, y, z = map(int, raw_input().split())
    cost = 0
    if x == y:
        cost += (b*x + w*y)
    if x < y:
        cost += b*x
        if y < z+x:
            cost += w*y
        else:
            cost += w*(x+z)
    if y < x:
        cost = w*y
        if x < z+y:
            cost += b*x
        else:
            cost += b*(y+z)
    print cost
