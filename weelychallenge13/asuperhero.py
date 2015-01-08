t = input()


def bulletsCheck(powerMatrix, bulletMatrix, n, m, bulletsStart):
    bulletsGained = [0]
    for x in xrange(n):
        bulletsForLevel = bulletsGained.pop()
        if min(powerMatrix[x]) > bulletsForLevel + bulletsStart:
            return False
        else:
            if min(powerMatrix[x]) <= bulletsForLevel:
                bulletsForLevel -= min(powerMatrix[x])
            elif min(powerMatrix[x]) <= bulletsForLevel + bulletsStart:
                bulletsStart -= min(powerMatrix[x]) - bulletsForLevel
        indexHold = powerMatrix[x].index(min(powerMatrix[x]))
        bulletsGained.append(bulletMatrix[x][indexHold])
    return True


def minBullets(powerMatrix, bulletMatrix, n, m):
    bulletsStart = 0
    while(not bulletsCheck(powerMatrix, bulletMatrix, n , m, bulletsStart)):
        bulletsStart += 1
    print bulletsStart



for x in xrange(t):
    n, m = map(int, raw_input().split())
    powerMatrix = [[0 for x in range(m)] for x in range(n)]
    bulletMatrix = [[0 for x in range(m)] for x in range(n)]
    for i in xrange(n):
        arrayPower = raw_input().split()
        for j in xrange(m):
            powerMatrix[i][j] = int(arrayPower[j])
    for i in xrange(n):
        arrayBullet = raw_input().split()
        for j in xrange(m):
            bulletMatrix[i][j] = int(arrayBullet[j])
    minBullets(powerMatrix, bulletMatrix, n, m)
