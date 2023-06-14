import random


pack_items = ["палатка", "удочка", "фонарь", "аптечка", "клмн", "сидушка", "котелок", "спички", "гитара", "сухпаек", 
              "рация", "аккумуллятор на солнечной панели", "карта", "вода", "фильтр", "спальник", "коврик", "фляшка", "сигнальная ракета", "фотоаппарат"]
# клмн - кружка, ложка, миска, ножик
names_1 = ["Миша", "Петя", "Вася", "Катя", "Ира", "Настя", "Инга", "Даня", "Леша"]





def find_items_everybody_has(input_dict):
    items_everybody_has = set()
    for value in input_dict.values():
        items_everybody_has = items_everybody_has.union(value)
    for value in input_dict.values():
        items_everybody_has = items_everybody_has & set(value)
    return items_everybody_has

def find_unique_items(input_dict):
    total_items = []
    result_list_of_unique_items = []
    for value in input_dict.values():
        for j in range(len(value)):
            total_items.append(value[j])
    set_of_total_ites = set(total_items)
    for item in set_of_total_ites:
        if  total_items.count(item) == 1:
            result_list_of_unique_items.append(item)
    return set(result_list_of_unique_items)

def find_items_everybody_except_one_has(input_dict):
    items_everybody_has = find_items_everybody_has(input_dict)
    unique_items = find_unique_items(input_dict)
    total_items = []
    result_dict = {}
    for value in input_dict.values():
        for j in range(len(value)):
            total_items.append(value[j]) 
    result_list_of_items = set(total_items) - items_everybody_has - unique_items
    for key, value in input_dict.items():
         for item in result_list_of_items:
             if item not in value:
                 result_dict[key] = item
    return result_dict

def trip(number_of_people: int, number_of_items: int):
    
    travel_dict = {}

    while len(travel_dict) < number_of_people:
        travel_dict[random.sample(names_1, k=1)[0]] = (random.sample(pack_items, k=number_of_items))
    print(travel_dict) # для проверки правильности решения

    items_everybody_has = find_items_everybody_has(travel_dict)
    if not items_everybody_has:
        items_everybody_has = None
    unique_items = find_unique_items(travel_dict)
    if not unique_items:
        unique_items = None
    item_everybody_except_one_has = find_items_everybody_except_one_has(travel_dict)
    if not item_everybody_except_one_has:
        item_everybody_except_one_has = None
    
    return items_everybody_has, unique_items, item_everybody_except_one_has

print(trip(3, 3))
