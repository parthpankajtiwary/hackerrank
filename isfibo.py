from math import sqrt

t = input()
inputs = []
for x in xrange(t):
    inputs.append(int(raw_input()))

for x in inputs:
    factorOne = 5*(x)**2 + 4
    factorTwo = 5*(x)**2 - 4
    valueOne = "%.1f" % (int(sqrt(factorOne))*int(sqrt(factorOne)))
    valueTwo = "%.1f" % (int(sqrt(factorTwo))*int(sqrt(factorTwo)))
    testOne = (float(valueOne) == float(factorOne)) 
    testTwo = (float(valueTwo) == float(factorTwo))
    if testOne or testTwo:
        print "IsFibo"
    else:
        print "IsNotFibo"       