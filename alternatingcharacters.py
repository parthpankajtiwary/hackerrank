t = input()
inputs = []

for x in range(t):
    inputs.append(raw_input())

for input in inputs:
    # scan the input from the left and keep the string if one string is different than other else delete it
    previousState = input[0]
    deletions = 0
    for x in xrange(1, len(input)):
        if input[x] != previousState:
            previousState = input[x]
        else:
            deletions += 1
            previousState = input[x]
    print deletions            