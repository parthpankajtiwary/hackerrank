def max_toys(prices, rupees):
    answer = 0
    prices.sort(key = lambda x: int(x))
    sum = 0
    for x in prices:
        if sum + int(x) <= int(rupees):
            sum += int(x)
            answer += 1
    return answer

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)