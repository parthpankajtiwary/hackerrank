t = input()
n = []
a = []
b = []
for x in range(t):
    n.append(input())
    a.append(input())
    b.append(input())

def outputs(n, a, b):
    result = ''
    if a == b:
        print (n - 1)*a
    else:
        result = sorted([str(max(a,b)*(n-1-i) + min(a,b)*i) for i in range(n)], key=lambda x: int(x))
        finalResult = []
        finalResult = [x for x in result if x not in finalResult]
        print " ".join(finalResult)
        
for x in range(t):
    outputs(n[x], a[x], b[x])