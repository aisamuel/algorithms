from collections import namedtuple

items = namedtuple('items', ['weight', 'value'])

def knapsack(weight, value, capacity):

    item_list = []

    for i in range(len(weight)):
        item_list.append(items(weight[i], value[i]))

    return knapsack_max_value(capacity, item_list)

def knapsack_max_value(knapsack_max_weight, items):

    lookup_table = [0] * (knapsack_max_weight + 1)

    for item in items:
        for capacity in reversed(range(knapsack_max_weight + 1)):
            print(lookup_table)
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity-item.weight] + item.value)

    return lookup_table[-1]

print(knapsack([2,1,1,3], [2,8,1,10], 4))