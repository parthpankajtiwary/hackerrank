
t = input()
inputs = []
for x in range(t):
	inputs.append(input())

for input in inputs:
		#maximize n in the equation 5n + 3m = input
		result = []
		result = [[n,m] for n in range(input + 1) for m in range(input + 1) 
					if n+m == input and (n%3 == 0 and m%5 == 0)]
		if result == []:
			print -1
		else:
			print "5"*result[0][0] + "3"*result[0][1]
				
			
				