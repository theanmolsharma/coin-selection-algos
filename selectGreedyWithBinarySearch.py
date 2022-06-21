def selectCoins(coins, target):
    ind = len(coins) - 1
    selected = []

    # while target is greater than
    # the largest coin we have, we
    # will keep selecting the largest coin
    while target >= coins[ind].value:
        selected.append(coins[ind])
        target -= coins[ind].value
        ind -= 1

    # we have reached the target, return selected
    if target == 0:
        return selected

    # now we are sure that
    # target < largest unselected coin
    # we will perform Binary search to
    # find the coin which is closest to target value
    closest = findClosest(coins, ind + 1, target)
    selected.append(closest)

    return selected


def findClosest(coins, n, target):
    # Corner cases
    if target <= coins[0].value:
        return coins[0]
    if target >= coins[n - 1].value:
        return coins[n - 1]

    # start binary search
    i = 0
    j = n
    mid = 0
    while i < j:
        mid = (i + j) // 2

        # exact match found, return
        if coins[mid] == target:
            return coins[mid]

        # If target is less than array
        # element, then search in left
        if target < coins[mid].value:
            # If target is greater than previous
            # to mid, return mid
            if mid > 0 and target > coins[mid - 1].value:
                return coins[mid]
            # Repeat for left half
            j = mid
        # If target is greater than mid
        else:
            # update i
            i = mid + 1

    # Only single element left after search
    return coins[mid]


class Coin():
    def __init__(self, value):
        self.value = value


coins = [Coin(1), Coin(10), Coin(20), Coin(50), Coin(80), Coin(99), Coin(100)]

targets = [100, 101, 200, 11, 30, 80]

for t in targets:
    print()
    print("target: " + str(t))
    input = 0
    print("coins: ", end="")
    for c in selectCoins(coins, t):
        input += c.value
        print(c.value, end=" ")
    print()
    print("change: " + str(input - t))