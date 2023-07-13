# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку

        
def conole_input():
    return input("Введите дату: ")


def _leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True


def my_date():
    day, month, year = list(map(int, conole_input().split('.')))
    if 1 <= year <= 9999 and 1 <= month < 13 and 1 <= day <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif month == 2 and 1 <= day <= 28:
            return True
        else:
            return _leap_year(year) and day <= 29
        
print(my_date())