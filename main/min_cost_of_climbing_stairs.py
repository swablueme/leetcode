from typing import List
import functools


def minCostClimbingStairs(cost):
    foundTotalCosts = []

    paths = {}

    @functools.lru_cache()
    def climb(cost: List[int], i=0, totalCost=0, path=()) -> int:
        if i > len(cost) - 1:
            if path not in paths:
                paths[path] = totalCost
            else:
                print(path, "already taken!")
            foundTotalCosts.append(totalCost)
            return

        if i == 0:
            j = 1
            foundCost = cost[j]
            climb(
                cost, j + 1, totalCost + foundCost, path + (f"{j} => {j+1}", ))
            climb(
                cost, j + 2, totalCost + foundCost, path + (f"{j} => {j+2}",))
        foundCost = cost[i]
        climb(
            cost, i + 1, totalCost + foundCost, path + (f"{i} => {i+1}", ))
        climb(
            cost, i + 2, totalCost + foundCost, path + (f"{i} => {i+2}", ))
    climb(tuple(cost))
    print(foundTotalCosts)
    return min(foundTotalCosts)


assert minCostClimbingStairs([1, 2]) == 1
assert minCostClimbingStairs([1, 2, 3]) == 2
assert minCostClimbingStairs([1, 2, 1, 2, 1, 1, 1]) == 4
