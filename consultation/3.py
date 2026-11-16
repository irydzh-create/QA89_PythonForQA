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