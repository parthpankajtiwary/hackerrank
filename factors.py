from math import sqrt



def factors(n):
	factorsList = []
	for x in xrange(2, int(sqrt(n)) + 1):
		while(n%x == 0):
			print x
			n /= x 
	if n > 1:
		print n		
	
	
factors(192)			