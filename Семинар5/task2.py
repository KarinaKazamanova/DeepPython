# ✔Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии


def bonus_count(names, wages, bonus_rates):
    parsed_bonus_rates = [float(i.split("%")[0]) for i in bonus_rates]
    bonuses = list(map(lambda x, y: x * y / 100, wages, parsed_bonus_rates))
    return {names[i]: bonuses[i] for i in range(len(names))}  



names = ["John", "Peter", "Bob"]
wages=  [10_000, 50_000, 15_000]
bonus_rates = ["10.6%", "34.25%", "0.1%"]

print(bonus_count(names, wages, bonus_rates))


