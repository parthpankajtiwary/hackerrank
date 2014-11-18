N = int(raw_input())

weight = raw_input().split()
weight.sort(key = lambda x: int(x))
brought = [weight[0]]
free = []
number = 1
for x in weight:
    if x != brought[-1]:
        if int(x) >= int(brought[-1]) and int(x) <= int(brought[-1]) + 4:
            free.append(x)
        else:
            brought.append(x)
            number += 1
print number
