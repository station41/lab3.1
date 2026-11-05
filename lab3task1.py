import math

# ввод данных
print('Введите Xbeg, Xend и Dx')
xb = float(input('Xbeg = '))
xe = float(input('Xend = '))
dx = float(input('Dx = '))

# шапка таблицы
print("+----------+----------+")
print("I    X     I    Y     I")
print("+----------+----------+")

# начинаем с начального значения
xt = xb

# цикл
while xt <= xe:
    # вычисление функции
    if xt <= -6:
        y = 2
    elif xt <= -2:
        y = 0.5 * xt + 1
    elif xt <= 0:
        y = 2 - math.sqrt(4 - (xt + 2) ** 2)
    elif xt <= 2:
        y = math.sqrt(4 - xt ** 2)
    elif xt <= 3:
        y = -xt + 2
    else:
        y = 0

    # вывод строки таблицы (форматируем до 2 знаков)
    print(f"I {xt:8.2f} I {y:8.2f} I")

    # шаг
    xt += dx

# низ таблицы
print("+----------+----------+")