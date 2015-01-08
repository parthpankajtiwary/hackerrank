#!/bin/python
def displayPathtoPrincess(n,grid):
    gridString = "|".join(grid)
    gridArray = gridString.split("m")
    for x in gridArray:
        if "p" in x:
            answerArray = x.split("p")
            if gridString.index("m") > gridString.index("p"):
                answerString = answerArray[1]
                for x in xrange(answerString.count("|")):
                    print "UP"
            else:
                answerString = answerArray[0]
                for x in xrange(answerString.count("|")):
                    print "DOWN"
    indexMoves = gridString.split("|")
    for x in indexMoves:
        if "m" in x:
            mIndex = x.index("m")
        if "p" in x:
            pIndex = x.index("p")

    deltaIndex = mIndex - pIndex
    if deltaIndex > 0:
        for x in xrange(deltaIndex):
            print "LEFT"
    if deltaIndex < 0:
        for x in xrange(abs(deltaIndex)):
            print "RIGHT"

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())




displayPathtoPrincess(m,grid)
