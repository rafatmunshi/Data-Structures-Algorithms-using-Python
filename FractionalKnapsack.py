class Item:
    def __init__(self, weight, value, index):
        self.weight = weight
        self.value = value
        self.index = index
        self.cost = value // weight

    def __lt__(self, other):
        return self.cost < other.cost


class FractionalKnapsack:
    def getMaxValue(weights, values, capacity):
        allItems = []
        for i in range(len(weights)):
            allItems.append(Item(weights[i], values[i], i))
        allItems.sort(reverse=True)
        totalValue = 0
        for item in allItems:
            currWeight = int(item.weight)
            currValue = int(item.value)
            if capacity - currWeight >= 0:
                capacity -= currWeight
                totalValue += currValue
            else:
                fraction = capacity / currWeight
                totalValue += int(currValue * fraction)
                break
        return totalValue


weights = [40, 10, 20, 24]
values = [280, 100, 120, 120]
# cost- 7, 10, 6, 5
# 100+280+60= 440
capacity = 60
print(FractionalKnapsack.getMaxValue(weights, values, capacity))
