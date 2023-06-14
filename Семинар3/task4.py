from itertools import chain, combinations

items = {'Спальник': 5.0,
         'Палатка': 10.0,
         'Топор': 2.5,
         'Еда': 7.0,
         'Вода': 5.0,
         'Бадминтон': 1.5,
         'Радио': 3.0}


def max_cargo(inventory: dict[str, float], capacity: int) -> list[list[str], float]:
    backpack = [[], 0]
    for item, weight in inventory.items():
        if backpack[1] + weight <= capacity:
            backpack[0].append(item)
            backpack[1] += weight
        else:
            break
    return backpack


print(max_cargo(items, 30))


def powerset(inventory: list[str]):
    return chain.from_iterable(combinations(inventory, r) for r in range(len(inventory) + 1))


def all_options(inventory: dict[str, float], capacity: int):
    result = []
    for cur_option in powerset(list(inventory)):
        if cur_option:
            weight = 0
            for item in cur_option:
                weight += inventory.get(item)
            if weight <= capacity and weight > capacity - min(inventory.values()):
                result.append((cur_option, weight))
    return result


for option in all_options(items, 30):
    print(option)