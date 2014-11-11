t = input()

def GCD(a,b):
	""" The Euclidean Algorithm """
	a = abs(a)
	b = abs(b)
        while a:
                a, b = b%a, a
        return b
        
        
def GCD_List(list):
	""" Finds the GCD of numbers in a list.
	Input: List of numbers you want to find the GCD of
		E.g. [8, 24, 12]
	Returns: GCD of all numbers
	"""
	return reduce(GCD, list)


results = []
for x in range(t):
    size = input()
    list = [int(x) for x in raw_input().split()]
    if GCD_List(list) > 1:
        results.append("NO")
    else:
        results.append("YES")

for result in results:
    print result