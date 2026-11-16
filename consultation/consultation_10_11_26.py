# Задание 1

def print_list_reverse(lst):  # создаём функцию с параметром lst (список)

    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        # lst is None — проверяем, равен ли lst значению None
        # or — ИЛИ, достаточно выполнения одного условия
        # not isinstance(lst, list) — lst НЕ является списком (list)
        # or — ИЛИ
        # len(lst) == 0 — проверяем, пустой ли список (0 элементов)

        print("Wrong list")  # выводим сообщение Wrong list в консоль
        return  # завершаем функцию, дальнейший код не выполняется

    reversed_lst = lst[::-1]
    # reversed_lst — переменная для хранения перевёрнутого списка
    # lst[::-1] — создаём новый список с элементами в обратном порядке
    # [start:stop:step] — формат среза списка
    # step = -1 — двигаемся по списку с конца к началу

    print(reversed_lst)  # выводим перевёрнутый список в консоль


# ТЕСТЫ

print_list_reverse([1, 2, 3, 4, 5])  # вывод: [5, 4, 3, 2, 1]

print_list_reverse([])  # вывод: Wrong list, потому что список пустой

print()  # выводим пустую строку (переход на новую строку)

#===========Задание 2============================
def is_valid_point(point):  # создаём функцию с параметром point

    if point is None:  # если point равен None
        return None  # возвращаем None и завершаем функцию

    if isinstance(point, tuple) and len(point) == 0:
        # isinstance(point, tuple) — проверяем, является ли point кортежем
        # and — И, оба условия должны выполняться
        # len(point) == 0 — количество элементов равно нулю
        return None  # возвращаем None

    if not isinstance(point, tuple) or len(point) != 2:
        # not isinstance(point, tuple) — point НЕ является кортежем
        # or — ИЛИ, достаточно одного выполненного условия
        # len(point) != 2 — количество элементов НЕ равно двум
        return False  # возвращаем False

    x, y = point  # распаковываем кортеж: x — первый, y — второй элемент

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        # not isinstance(x, (int, float)) — x НЕ является int или float
        # or — ИЛИ
        # not isinstance(y, (int, float)) — y НЕ является int или float
        return False  # возвращаем False

    return True  # все проверки пройдены, возвращаем True


#=======задание 3==================
def print_sublist_reverse(lst, start, finish):
    # создаём функцию с тремя параметрами:
    # lst — список, start — начальный индекс, finish — конечный индекс

    if not isinstance(lst, list) or len(lst) == 0:
        # not isinstance(lst, list) — lst НЕ является списком
        # or — ИЛИ
        # len(lst) == 0 — список пустой (0 элементов)
        print("Wrong args")  # выводим сообщение Wrong args в консоль
        return  # завершаем функцию, дальше код не выполняется

    if type(start) is not int or type(finish) is not int:
        # type(start) is not int — start НЕ имеет тип int
        # or — ИЛИ
        # type(finish) is not int — finish НЕ имеет тип int
        print("Wrong args")  # выводим сообщение об ошибке
        return  # завершаем функцию

    if start < 0 or finish >= len(lst) or start > finish:
        # start < 0 — начальный индекс меньше нуля
        # or — ИЛИ
        # finish >= len(lst) — конечный индекс больше или равен длине списка
        # or — ИЛИ
        # start > finish — начальный индекс больше конечного
        print("Wrong args")  # выводим сообщение об ошибке
        return  # завершаем функцию

    first_part = lst[:start]
    # lst[:start] — берём элементы от начала до start, не включая start

    middle_part = lst[start:finish + 1]
    # lst[start:finish + 1] — берём элементы от start до finish включительно
    # + 1 — нужен, потому что правая граница среза не включается

    last_part = lst[finish + 1:]
    # lst[finish + 1:] — берём элементы после finish до конца списка

    middle_part = middle_part[::-1]
    # [::-1] — переворачиваем среднюю часть в обратном порядке

    result = first_part + middle_part + last_part
    # + — соединяем три списка в один

    print(result)  # выводим готовый список в консоль
