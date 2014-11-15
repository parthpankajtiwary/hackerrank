n = int(raw_input())
numbers = []
for x in range(n):
    numbers.append(raw_input())

for number in numbers:
    length = len(number)
    count = 0
    for x in range(length): # Loop for extracting individual digits
        n = int(number[x])
        if n != 0:
            if int(number)%n == 0:
                count += 1
    print count 