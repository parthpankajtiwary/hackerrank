n = input()

listCycles = []
listHeights = []

while n > 0:
    cycles = input()
    listCycles.append(cycles)
    n -= 1

    

for i in listCycles:
    cycle = 1
    height = 1
    if i != 0:
        while cycle <= i:
            if cycle%2 == 1:
                height *= 2
            if cycle%2 == 0 and cycle != 0:
                height += 1
            cycle += 1
    else:
        height = height
    listHeights.append(height)

for i in listHeights:
    print i