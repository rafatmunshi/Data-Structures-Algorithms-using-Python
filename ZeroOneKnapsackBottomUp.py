def knapsack(W, weights, values, n):
    dptable=[[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w ==0:
                dptable[i][w] = 0
            elif weights[i-1] <= w:
                dptable[i][w]= max(values[i-1]+dptable[i-1][w-weights[i-1]], dptable[i-1][w])
            else:
                dptable[i][w]= dptable[i-1][w]
    return dptable[n][W]

weights = [1, 2, 3]
values = [1, 6, 10]
W = 4
n = len(values)
print(knapsack(W, weights, values, n))