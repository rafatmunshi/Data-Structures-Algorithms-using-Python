weights = [1, 2, 3]
values = [1, 6, 10]
W = 4
n = len(values)

dptable= [[-1 for i in range(W+1)] for j in range(n+1)]

def knapsack(W, weights, values, n):
    if n == 0 or W == 0:
        return 0
    #memoization
    if dptable[n][W] != -1:
        return dptable[n][W]

    if weights[n - 1] > W:
        dptable[n][W] = knapsack(W, weights, values, n - 1)
        return dptable[n][W]
    # case 1- nth item is included
    # case 2- nth item is not included
    else:
        dptable[n][W] = max(values[n - 1] + knapsack(W - weights[n - 1], weights, values, n - 1),
                   knapsack(W, weights, values, n - 1))
        return dptable[n][W]

print(knapsack(W, weights, values, n))

