from math import sqrt, ceil, floor

t = input()
a = []
b = []
for x in range(t):
    A, B = map(int, raw_input().split())
    a.append(A)
    b.append(B)
for x in range(t):
    print int(floor(sqrt(b[x])) + 1 - ceil(sqrt(a[x]))