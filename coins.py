import timeit
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [0] + [float('inf')]*amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    result = {}
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                amount -= coin
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                break
    return result

setup_code = """
from __main__ import find_coins_greedy, find_min_coins
"""

# Приклад використання:
greedy_timeit = timeit.timeit("find_coins_greedy(113)", setup=setup_code, number=200)
dp_timeit = timeit.timeit("find_min_coins(113)", setup=setup_code, number=200)
greedy_result = find_coins_greedy(113)
dp_result = find_min_coins(113)

print("Жадібний алгоритм:", greedy_result,  "Час ", greedy_timeit)
print("Динамічне програмування:", dp_result, "Час ", dp_timeit)

