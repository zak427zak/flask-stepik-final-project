# Определение правильного окончания
def plural_days(n, what, text_only):
    if what == 'steps':
        days = ['шаг', 'шага', 'шагов']

    if n % 10 == 1 and n % 100 != 11:
        p = 0
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        p = 1
    else:
        p = 2

    if text_only:
        return days[p]
    else:
        return str(n) + ' ' + days[p]


# Вывод выбранного направления в текстовом виде
def get_direction(way):
    directions = {1: "Север", 2: "Восток", 3: "Юг", 4: "Запад"}
    return directions[way]
