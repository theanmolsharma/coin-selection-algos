TOTAL_TRIES = 100000


def selectBnB(coins, target):
    selected = []
    currValue = 0

    # calculate total available value
    totalValue = 0
    for coin in coins:
        totalValue += coin.value

    # we don't have enough balance
    if totalValue < target:
        return []

    # sort the coins
    coins.sort(key=lambda x: x.value, reverse=True)

    currTry = 0
    utxo_pool_index = 0

    # perform a depth-first search for choosing UTXOs
    while currTry < TOTAL_TRIES:
        backtrack = False
        # conditions for backtracking
        # 1. cannot reach target with remaining amount
        # 2. selected value is greater than upperbound
        if currValue + totalValue < target or currValue > target:
            backtrack = True
        # if selected value is equal to target, we are done
        elif currValue == target:
            break

        # backtrack if necessary
        if backtrack:
            # we walked back to first UTXO,
            # all branches are traversed, we are done
            if len(selected) == 0:
                break

            # Add omitted UTXOs back before traversing the omission branch of last included UTXO.
            utxo_pool_index -= 1
            while utxo_pool_index > selected[-1]:
                totalValue += coins[utxo_pool_index].value
                utxo_pool_index -= 1

            # Remove last included UTXO from selected list.
            currValue -= coins[utxo_pool_index].value
            selected.pop()
        # continue on this branch, add the next UTXO to selected list
        else:
            coin = coins[utxo_pool_index]
            # remove this UTXO from total available amount
            totalValue -= coin.value
            # if this UTXO is the first one or
            # if the previous index is included and therefore not relevant for exclusion shortcut or
            # if this UTXO's value is different from the previous one,
            if len(selected) == 0 or utxo_pool_index - 1 == selected[-1] or coin.value != coins[utxo_pool_index - 1].value:
                selected.append(utxo_pool_index)
                currValue += coins[utxo_pool_index].value

        currTry += 1
        utxo_pool_index += 1

    # if we exhausted all tries, return empty list
    if currTry >= TOTAL_TRIES:
        return []

    # return the selected UTXOs
    result = []
    for i in selected:
        result.append(coins[i])
    return result


class Coin():
    def __init__(self, value):
        self.value = value


coins = [Coin(1), Coin(10), Coin(20), Coin(50), Coin(80), Coin(99), Coin(100)]

targets = [100, 101, 200, 11, 12, 30, 80, 1000]

for t in targets:
    print()
    print("target: " + str(t))
    input = 0
    res = selectBnB(coins, t)
    if len(res) == 0:
        print("No exact solution possible!!")
        continue
    print("coins: ", end="")
    for c in res:
        input += c.value
        print(c.value, end=" ")
    print()
    print("change: " + str(input - t))



